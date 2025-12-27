import json

def main():
    transactions = json.loads(input("Enter data: "))

    rates = {
        "EUR": 1.18,
        "INR": 0.012,
        "USD": 1.0
    }

    converted = list(
        map(
            lambda t: {
                "status" : t["status"],
                "amount" : t["amount"] * rates[t["currency"]]
            },
            transactions
        )
    )

    output = {
        status : sum(txn["amount"] for txn in converted if txn["status"] == status)
        for status in {"success", "failed"}
    }

    print(output)

main()