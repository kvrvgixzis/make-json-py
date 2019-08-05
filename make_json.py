import json
import os

def making_JSON():
    indir = '/home/kvv/Python/Data/natural_movies_gaze'
    outdir = '/home/kvv/Python/Data/natural_movies_gaze_jsons/'
    Ts = X = Y = 0.0

    for root, _, filenames in os.walk(indir):
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

            print(f, 'JSON maked')

    print('\n\n\nJSON creation complete!\n\n')


def making_dirs():
    indir = '/home/kvv/Python/Data/movies_mpg'
    outdir = '/home/kvv/Python/Data/output_data/'

    for _, _, filenames in os.walk(indir):
        for f in filenames:
            video_name = f.split(".")[0]
            os.system("ffmpeg -i " + indir + "/" + video_name + ".mpg " + indir + "/" + video_name + ".mp4")
            os.system("rm " + indir + "/" + video_name + ".mpg")

            print('\n\n\n' + video_name, 'converted\n\n')

            os.system("mkdir " + outdir + video_name)

            # mv video to new dir
            # mv JSONs to new dir using mask

    print('\n\n\nDirs creation complete!\n\n')


if __name__ ==  "__main__":
    making_JSON()
    making_dirs()