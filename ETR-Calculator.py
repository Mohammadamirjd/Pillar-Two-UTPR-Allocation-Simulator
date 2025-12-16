import pandas as pd


def calculate_utpr_allocation(
    file_path,
    residual_top_up_tax,
    payroll_weight=0.5,
    asset_weight=0.5
):
    """
    Calculates the allocation of residual top-up tax under the UTPR
    based on payroll and tangible asset factors.

    Parameters
    ----------
    file_path : str
        Path to the CSV file containing UTPR allocation factors.
    residual_top_up_tax : float
        Total residual top-up tax amount to be allocated.
    payroll_weight : float, optional
        Weight assigned to the payroll factor (default is 0.5).
    asset_weight : float, optional
        Weight assigned to the tangible asset factor (default is 0.5).

    Returns
    -------
    pandas.DataFrame
        DataFrame containing allocation shares and allocated UTPR tax.
    """

    # Validate that allocation weights sum to 1 (tolerant to floating-point precision)
    if not abs(payroll_weight + asset_weight - 1) < 1e-9:
        raise ValueError("Payroll and asset weights must sum to 1.")

    # Residual top-up tax must be non-negative
    if residual_top_up_tax < 0:
        raise ValueError("Residual top-up tax must be non-negative.")

    # Load input data
    df = pd.read_csv(file_path)

    # Ensure the input file contains data
    if df.empty:
        raise ValueError("Input file contains no data.")

    # Check for required columns
    required_columns = {'Employees', 'Tangible_Assets'}
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    # Convert numeric columns and coerce invalid values to NaN, then replace with zero
    df['Employees'] = pd.to_numeric(df['Employees'], errors='coerce').fillna(0)
    df['Tangible_Assets'] = pd.to_numeric(df['Tangible_Assets'], errors='coerce').fillna(0)

    # Negative values are not economically meaningful in this context
    if (df['Employees'] < 0).any() or (df['Tangible_Assets'] < 0).any():
        raise ValueError("Employees and Tangible Assets must be non-negative.")

    # Aggregate total payroll and asset bases
    total_employees = df['Employees'].sum()
    total_assets = df['Tangible_Assets'].sum()

    # Validate consistency between weights and available factors
    if total_employees == 0 and payroll_weight > 0:
        raise ValueError("Payroll weight is positive but no employees were reported.")
    if total_assets == 0 and asset_weight > 0:
        raise ValueError("Asset weight is positive but no tangible assets were reported.")

    # Compute factor shares (safe-guarded against division by zero)
    df['Payroll_Share'] = (
        df['Employees'] / total_employees if total_employees > 0 else 0
    )
    df['Asset_Share'] = (
        df['Tangible_Assets'] / total_assets if total_assets > 0 else 0
    )

    # Calculate the combined allocation weight
    df['Allocation_Weight'] = (
        payroll_weight * df['Payroll_Share']
        + asset_weight * df['Asset_Share']
    )

    # Allocate the residual top-up tax proportionally
    df['Allocated_UTPR_Tax'] = df['Allocation_Weight'] * residual_top_up_tax

    # Adjust for rounding differences to ensure full allocation of the tax amount
    rounding_difference = (
        residual_top_up_tax - df['Allocated_UTPR_Tax'].round(2).sum()
    )
    df.loc[df.index[-1], 'Allocated_UTPR_Tax'] += rounding_difference

    # Final rounding for reporting purposes
    df['Allocated_UTPR_Tax'] = df['Allocated_UTPR_Tax'].round(2)

    return df
