    inputs = " ".join(distances)
    os.system("cd HyperbolicAlgorithm/")
    os.system("g++ HyperbolicAlgorithm/*.cpp -o HyperbolicAlgorithm/output" )
    result = os.popen("./HyperbolicAlgorithm/output 1 " + inputs).readlines()
    
    return [result[0].rstrip("\n"), result[1].rstrip("\n")]
