x = 0
count = 0
days = ["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth","Eleventh","Twelfth"]
numbers = ["A", "Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve"]
stuff = ["Partridge in a Pear Tree.","Turtle Doves, and","French Hens,","Calling Birds,","Gold Rings,","Geese-a-Laying,","Swans-a-Swimming,","Maids-a-Milking,","Ladies Dancing,","Lords-a-Leaping,","Pipers Piping,","Drummers Drumming,"]
while x < 12:
 print("On the " + days[x] + " day of Christmas")
 print("My true love sent to me")
 while count >= 0:
  print(numbers[count] + " " +stuff[count])
  count -= 1
 x += 1
 count = x
 print(" ")
