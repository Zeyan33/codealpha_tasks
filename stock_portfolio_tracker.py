print("-" * 60)
print("     STOCK PORTFOLIO TRACKER")
print("-" * 60)

stocks = {
  "AAPL": 190,
  "AMZN": 160,
  "TCS": 90,
  "MSFT": 180,
  "TSLA": 170,
  "NVDA": 220,
  "GOOGL": 240
}

portfolio = {}
total_portfolio_value = 0

print("\nAvailable stocks")

for stock in stocks:
    print(stock,"=",stocks[stock])
    
while True:
 stock_name = input("\nEnter stock name: ").upper()
 
 if stock_name in stocks:
     quantity = int(input("Enter quantity: "))
     
     stock_value = stocks[stock_name]* quantity
     portfolio[stock_name] = quantity
     
     total_portfolio_value += stock_value 
     
     print("\nAdded Successfully!")
     print("Investment Value =", stock_value)
     
 else:
     print("Stock not found")
     
 choice = input("\nDo you want to add another stock? (yes/no): ").lower()   
 
 if choice != "yes":
     break
          
print("="* 30)  
print("        PORTFOLIO SUMMARY")
print("=" * 30)

for stock in portfolio:
 print(stock,":",portfolio[stock],"shares")
 
print("\nTotal Portfolio Value = ", total_portfolio_value)
 
  
 
 
     
     
         
         