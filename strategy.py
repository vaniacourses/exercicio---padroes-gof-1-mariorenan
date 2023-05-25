class War:
    def Strategy(strategy):
        print("the was main strategy is ",strategy)

    def Strength(strength):
        print("the strength of the enemy is ", strength)

    def Start(start):
        print("the war started this way: ", start)
    
    def End(end):
        print("the war ended because of: ", end)
    
    class interfaceStrategy:
        def do_strategy(str):
            return str

    class interfaceStrength:
        def do_measure_strength(str):
            return str
    
    class interfaceStart:
        def do_determine_start(str):
            return str

    class interfaceEnd:
        def do_determine_end(str):
            return str


War.Start("Recuar tropas")
War.End("Desarmar inimigo")
War.Strength("Nuclear")
War.Strategy("Diplomacia")