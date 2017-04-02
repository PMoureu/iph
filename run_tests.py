
try:
    import iph
    from iph.tests import discover_and_run

    discover_and_run()

except Exception as e:
    print(e)
    import traceback
    traceback.print_exc()
a = raw_input('')