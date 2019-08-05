import json
import os
import ntpath

indir = '/home/kvv/Python/Data/natural_movies_gaze'
outdir = '/home/kvv/Python/Data/natural_movies_gaze_jsons/'
Ts, X, Y, s = 0.0, 0.0, 0.0, 0.0

for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        temp = 0
        export_data = []
        importfile = open(os.path.join(root, f), 'r')
        for lines in importfile:
            temp += 1
            if temp > 2:
                Ts, X, Y, s = lines.split()
                export_data.append({"X": float(X), "Y": float(Y), "Ts": float(Ts) / 1000.0}) 
        importfile.close()  

        print("sdfsd" , f)

        exportfile = open(outdir + ntpath.basename(f) + ".json", "w")
        exportfile.write(json.dumps(export_data))
        exportfile.close()

print("Done!")