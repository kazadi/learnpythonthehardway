name = 'Kazadi'
age = 24
height = 5 * 12 + 11 #inches
weight = 150 #lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'
heightcm = round(height * 2.54)
weightkg = round(weight * 0.453592)

print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( age, height, weight, age + height + weight)

print "height in cm %d, weight in kg %d" % (heightcm, weightkg)