try:
    import iph
    iph.go()
    #iph.debug()

except Exception as e:
    print(e)
    import traceback
    traceback.print_exc()

a = raw_input('Press enter to exit')

# tracer pattern
#import iph
#a = 1
#iph.snap(a)

#a += 1
#iph.snap(a)

#iph.go()
