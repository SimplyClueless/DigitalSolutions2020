Area = float(input("How big is the area you want to paint (feet): "))
PaintPrice = float(input("How much is it for a gallon of paint ($): "))

AmountOfPaint = Area / 112
Hours = AmountOfPaint / 12
PaintCost = PaintPrice * AmountOfPaint
Labour = Hours * 35
Total = PaintCost + Labour

print("You require", AmountOfPaint, "gallons of paint, requiring", Hours, "worth of labour hours")
print("With total labour costing", Labour, "and total paint costing", PaintCost, ", The total cost comes to", Total)
