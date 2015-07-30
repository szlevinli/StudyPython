my_name = 'levin li'
my_age = 38
my_height = 171  # cm
my_weight = 65.5  # kg
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's table about %s." % my_name
print "He's %d CM tall." % my_height
print "He's %d KG heavy." % my_weight
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on coffee" % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

print "Let's table about %r." % my_name
print "He's %r CM tall." % my_height
print "He's %r KG heavy." % my_weight
print "He's got %r eyes and %r hair." % (my_eyes, my_hair)
print "His teeth are usually %r depending on coffee" % my_teeth
