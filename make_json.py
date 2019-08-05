import json
import os

def making_JSON():
    indir = '/home/kvv/Python/Data/natural_movies_gaze'
    outdir = '/home/kvv/Python/Data/natural_movies_gaze_jsons/'
    Ts = X = Y = 0.0

    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            temp = 0
            export_data = []
            importfile = open(os.path.join(root, f), 'r')
            
            for lines in importfile:
                temp += 1
                if temp > 2:
                # reading from the third line
                    Ts, X, Y = lines.split()[:3]
                    export_data.append({"X": float(X), "Y": float(Y), "Ts": float(Ts) / 1000.0})
        
            exportfile = open(outdir + f + ".json", "w")
            exportfile.write(json.dumps(export_data))
            importfile.close() 
            exportfile.close()

    print('JSON creation complete!')

if __name__ ==  "__main__":
    making_JSON()