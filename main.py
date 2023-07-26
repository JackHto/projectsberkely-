def m_lb1():
    nouns = []
    for i in range(3):
        nouns.append(input("A noun: "))
        
        
    adj = []
    for x in range(3):
        adj.append(input("An adjective: "))
    
    verb = []
    for y in range(2):
        verb.append(input("A verb: "))
    
    print ("No animal must ever live in  a " + nouns[0])
    print ("or sleep  in a " + nouns[1] + ",or wear clothes")
    print ("or drink " + nouns[2] + ", or smoke tobacco")
    print ("or touch money, or engage in trade.")
    print ("The habits of Man are " + adj[0] + ". And, above")
    print ("all, no animal must ever " + verb[0] + "over his own")
    print("kind. Weak or " + adj[1] + ", clever or " + adj[2] + ", we are all brothers.")
    print( "No animal must ever " + verb[1] + " any other animal.")
    print("All animals are equal")
    
    
m_lb1()