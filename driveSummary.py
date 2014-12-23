#!/usr/bin/python
from sys import argv, stdout
from os import walk, path


def size_of_human(num):
        num = int(num)
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0



def main():
    data = {}
    wave_counter = 0
    mp3_counter = 0

    mov_counter = 0
    mp4_counter = 0
    avi_counter = 0

    tiff_counter = 0
    jpeg_counter = 0
    bmp_counter = 0
    gif_counter = 0
    png_counter = 0

    audio_counter = 0
    video_counter = 0
    image_counter = 0
    other_counter = 0

    md5_counter = 0
    total_counter = 0
    total_file_size = 0

    other_files = []

    #get the list of files from the given folder
    input_argument = str(argv[1])
    if not path.isdir(input_argument):
        print "Not Valid directory"
        return
    print "Checking: " + input_argument,
    stdout.flush()

    if path.isdir(input_argument):
        for root, dir, files in walk(input_argument):
            for file in files:
                if path.isfile(path.join(root, file)):
                    total_counter += 1
                    total_file_size += path.getsize(path.join(root, file))

                    if ".md5" in file:
                        md5_counter += 1
                        continue

                    elif ".wav" in file:
                        wave_counter += 1
                        audio_counter += 1
                        continue

                    elif ".mp3" in file:
                        mp3_counter += 1
                        audio_counter += 1
                        continue

                    elif ".mov" in file:
                        mov_counter += 1
                        video_counter += 1
                        continue

                    elif ".mp4" in file:
                        mp4_counter += 1
                        video_counter += 1
                        continue

                    elif ".avi" in file:
                        avi_counter += 1
                        video_counter += 1
                        continue

                    elif ".tif" in file:
                        tiff_counter += 1
                        image_counter += 1
                        continue

                    elif ".jpg" in file:
                        jpeg_counter += 1
                        image_counter += 1
                        continue

                    elif ".bmp" in file:
                        bmp_counter += 1
                        image_counter += 1
                        continue

                    elif ".gif" in file:
                        gif_counter += 1
                        image_counter += 1
                        continue

                    elif ".png" in file:
                        png_counter += 1
                        image_counter += 1
                        continue
                    else:
                        other_counter += 1
                        other_files.append(path.join(root, file))

    print "...done"
    # report
    print "/=========================== Non-AV files on drive: START ===========================\\"
    for other_file in other_files:
        print other_file
    print "\\=========================== Non-AV files on drive: END ===========================/"
    print "\n=================== AUDIO FILES ==================="
    print "The number of mp3 files are: \t\t" + str(mp3_counter)
    print "The number of wav files are: \t\t" + str(wave_counter)

    print "\n=================== VIDEO FILES ==================="
    print "The number of avi files are: \t\t" + str(avi_counter)
    print "The number of mov files are: \t\t" + str(mov_counter)
    print "The number of mp4 files are: \t\t" + str(mp4_counter)

    print "\n=================== IMAGE FILES ==================="
    print "The number of tif files are: \t\t" + str(tiff_counter)
    print "The number of jpg files are: \t\t" + str(jpeg_counter)
    print "The number of bmp files are: \t\t" + str(bmp_counter)
    print "The number of gif files are: \t\t" + str(gif_counter)
    print "The number of png files are: \t\t" + str(png_counter)

    print "\n===================== SUMMARY ====================="

    print "The number of video files are: \t\t" + str(video_counter)
    print "The number of audio files are: \t\t" + str(audio_counter)
    print "The number of image files are: \t\t" + str(image_counter)
    print "The number of MD5 checksum files are: \t" + str(md5_counter)
    print "The number of other files are: \t\t" + str(other_counter)
    print "The number of total files are: \t\t" + str(total_counter)

    print "The total size of tbe data is: \t\t" + str(size_of_human(total_file_size))
    print ""
if __name__ == '__main__':
    main()
