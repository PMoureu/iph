try:
    import iph
    iph.go()
    # iph.debug()

except Exception as e:
    print(e)
    import traceback
    traceback.print_exc()



# snapshots pattern:

#import iph

#a = UFO_object
#iph.snap(a)

#b = other_UFO_object
#iph.snap(b)

#iph.go()
