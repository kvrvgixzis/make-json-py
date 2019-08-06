import json
import os


def making_JSONs():
    indir = '/home/kvv/Python/Data/natural_movies_gaze'
    outdir = '/home/kvv/Python/Data/natural_movies_gaze_jsons/'
    Ts = X = Y = 0.0
    #making JSONs
    for _, _, filenames in os.walk(indir):
        for f in filenames:
            temp = 0
            export_data = []
            importfile = open("{}/{}".format(indir,f), 'r')          
            for lines in importfile:
                temp += 1
                if temp > 2:
                # reading from the third line
                    Ts, X, Y, _ = lines.split()
                    export_data.append({"X": float(X), "Y": float(Y), "Ts": float(Ts) / 1000.0})        
            exportfile = open("{}{}.json".format(outdir,f), "w")
            exportfile.write(json.dumps(export_data))
            importfile.close() 
            exportfile.close()
            print('{} JSON maked'.format(f))
    print('\n\n\nJSON creation complete!\n\n')


def convert_videos():
    indir = '/home/kvv/Python/Data/movies_mpg'
    outdir = '/home/kvv/Python/Data/output_data/'
    # convert video
    for _, _, filenames in os.walk(indir):
        for f in filenames:
            video_name = f.split(".")[0]
            os.system("ffmpeg -i {}/{}.mpg {}/{}.mp4".format(indir, video_name, indir, video_name))
            os.system("rm {}/{}.mpg".format(indir, video_name))
            print('\n\n\n{} converted\n\n'.format(video_name))
            # mkdir and mv video
            os.system("mkdir {}{}".format(outdir, video_name))
            os.system("mv {}/{}.mp4 {}{}/".format(indir, video_name, outdir, video_name))


def mv_files():
    indir = '/home/kvv/Python/Data/natural_movies_gaze_jsons/'
    outdir = '/home/kvv/Python/Data/output_data/'
    # mv JSONs
    for _, _, filenames in os.walk(indir):
        for f in filenames:
            json_name = f[4:-11]
            os.system("mv {}/{} {}{}/".format(indir,f, outdir, json_name))
            print('{} done!'.format(json_name))


if __name__ ==  "__main__":
    making_JSONs()
    convert_videos()
    mv_files()