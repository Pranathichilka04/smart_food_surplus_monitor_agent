# predictor.py

import pandas as pd
from datetime import datetime


def predict_surplus(csv_path="data/inventorydataset.csv", today=None):
    """
    Predicts surplus food items and recommends actions (Donate, Discount, Redistribute).
    Args:
        csv_path (str): Path to inventory CSV file.
        today (datetime.date): Custom today's date for simulation/testing. Defaults to actual today.
    Returns:
        List of dictionaries with surplus prediction and suggested actions.
    """
    # Load dataset
    df = pd.read_csv(csv_path)

    # Convert expiry_date to datetime.date format
    df["expiry_date"] = pd.to_datetime(df["expiry_date"]).dt.date

    # Set today's date
    if today is None:
        today = datetime.today().date()

    # Calculate days to expiry
    df["days_to_expiry"] = (df["expiry_date"] -
                            today).apply(lambda x: max(x.days, 0))

    # Predict demand until expiry
    df["predicted_demand"] = df["avg_daily_sales"] * df["days_to_expiry"]

    # Calculate surplus stock
    df["surplus_units"] = df["stock"] - df["predicted_demand"]

    # Suggest actions based on urgency
    def suggest_action(row):
        if row["surplus_units"] > 0:
            if row["days_to_expiry"] <= 2:
                return "Donate"
            elif row["days_to_expiry"] <= 4:
                return "Discount"
            else:
                return "Redistribute"
        return "No Action"

    df["suggested_action"] = df.apply(suggest_action, axis=1)

    # Filter only surplus cases
    result = df[df["surplus_units"] > 0][[
        "item", "store", "stock", "avg_daily_sales", "expiry_date",
        "shelf_life", "item_risk_level", "days_to_expiry", "predicted_demand",
        "surplus_units", "suggested_action"
    ]]

    # Optional: Export results to CSV for dashboard use
    result.to_csv("data/surplus_predictions.csv", index=False)

    return result.to_dict(orient="records")


# Run this when executing the script directly
if __name__ == "__main__":
    results = predict_surplus()
    print(f"\n📦 Total Surplus Items: {len(results)}\n")
    for item in results:
        print(item)
