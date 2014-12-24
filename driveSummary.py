#!/usr/bin/python
from sys import argv, stdout
from os import walk, path



def size_of_human(num):
    num = int(num)
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def report(data, other_files):
    print "/=========================== Non-AV files on drive: START ===========================\\"
    for other_file in other_files:
        print other_file
    print "\\=========================== Non-AV files on drive: END ===========================/"
    print "\n=================== AUDIO FILES ==================="
    if data["mp3_counter"] != 0:
        print "The number of mp3 files are: \t\t" + str(data["mp3_counter"])

    if data["wave_counter"] != 0:
        print "The number of wav files are: \t\t" + str(data["wave_counter"])

    print "\n=================== VIDEO FILES ==================="
    if data["avi_counter"] != 0:
        print "The number of avi files are: \t\t" + str(data["avi_counter"])

    if data["dv_counter"] != 0:
        print "The number of dv files are: \t\t" + str(data["dv_counter"])

    if data["mov_counter"] != 0:
        print "The number of mov files are: \t\t" + str(data["mov_counter"])

    if data["mp4_counter"] != 0:
        print "The number of mp4 files are: \t\t" + str(data["mp4_counter"])

    if data["m4v_counter"] != 0:
        print "The number of m4v files are: \t\t" + str(data["m4v_counter"])

    print "\n=================== IMAGE FILES ==================="
    if data["tiff_counter"] != 0:
        print "The number of tif files are: \t\t" + str(data["tiff_counter"])

    if data["jpeg_counter"] != 0:
        print "The number of jpg files are: \t\t" + str(data["jpeg_counter"])

    if data["bmp_counter"] != 0:
        print "The number of bmp files are: \t\t" + str(data["bmp_counter"])

    if data["gif_counter"] != 0:
        print "The number of gif files are: \t\t" + str(data["gif_counter"])

    if data["png_counter"] != 0:
        print "The number of png files are: \t\t" + str(data["png_counter"])

    print "\n================= DOCUMENT FILES =================="
    if data["excel_counter"] != 0:
        print "The number of excel files are: \t\t" + str(data["excel_counter"])

    if data["rtf_counter"] != 0:
        print "The number of rich text \"rtf\" files are:" + str(data["rtf_counter"])

    if data["doc_counter"] != 0:
        print "The number of doc files are: \t\t" + str(data["doc_counter"])

    if data["pdf_counter"] != 0:
        print "The number of pdf files are: \t\t" + str(data["pdf_counter"])

    print "\n===================== SUMMARY ====================="
    print "The number of video files are: \t\t" + str(data["video_counter"])
    print "The number of audio files are: \t\t" + str(data["audio_counter"])
    print "The number of image files are: \t\t" + str(data["image_counter"])
    print "The number of document files are: \t" + str(data["document_counter"])
    print "The number of MD5 checksum files are: \t" + str(data["md5_counter"])
    print "The number of other files are: \t\t" + str(data["other_counter"])
    print "The number of total files are: \t\t" + str(data["total_counter"])
    print "The total size of tbe data is: \t\t" + str(size_of_human(data["total_file_size"]))
    print ""


def get_data(input_argument):
    # get the list of files from the given folder
    data = {
        "wave_counter": 0,
        "mp3_counter": 0,
        "mov_counter": 0,
        "mp4_counter": 0,
        "m4v_counter": 0,
        "dv_counter": 0,
        "avi_counter": 0,
        "tiff_counter": 0,
        "jpeg_counter": 0,
        "bmp_counter": 0,
        "gif_counter": 0,
        "png_counter": 0,
        "excel_counter": 0,
        "rtf_counter": 0,
        "doc_counter": 0,
        "pdf_counter": 0,
        "audio_counter": 0,
        "video_counter": 0,
        "image_counter": 0,
        "document_counter": 0,
        "other_counter": 0,
        "md5_counter": 0,
        "total_counter": 0,
        "total_file_size": 0
    }
    otherFiles = []
    if path.isdir(input_argument):
        for root, dir, files in walk(input_argument):
            for file in files:
                if path.isfile(path.join(root, file)):
                    file_name, extention = path.splitext(file)
                    data["total_counter"] += 1
                    data["total_file_size"] += path.getsize(path.join(root, file))
                    if extention == ".md5":
                        data["md5_counter"] += 1
                        continue
# ---------------------------------------------- audio -----------------------------------------------------------------
                    elif extention.lower() == ".wav":
                        data["wave_counter"] += 1
                        data["audio_counter"] += 1
                        continue

                    elif extention.lower() == ".mp3":
                        data["mp3_counter"] += 1

                        data["audio_counter"] += 1
                        continue
# --------------------------------------------- video -----------------------------------------------------------------
                    elif extention.lower() == ".mov":
                        data["mov_counter"] += 1
                        data["video_counter"] += 1
                        continue

                    elif extention.lower() == ".mp4":
                        data["mp4_counter"] += 1
                        data["video_counter"] += 1
                        continue

                    elif extention.lower() == ".m4v":
                        data["m4v_counter"] += 1
                        data["video_counter"] += 1
                        continue

                    elif extention.lower() == ".avi":
                        data["avi_counter"] += 1
                        data["video_counter"] += 1
                        continue

                    elif extention.lower() == ".dv":
                        data["dv_counter"] += 1
                        data["video_counter"] += 1
                        continue
# ---------------------------------------------- image -----------------------------------------------------------------

                    elif extention.lower() == ".tif" or extention.lower() == ".tiff":
                        data["tiff_counter"] += 1
                        data["image_counter"] += 1
                        continue

                    elif extention.lower() == ".jpg" or extention.lower() == ".jpeg":
                        data["jpeg_counter"] += 1
                        data["image_counter"] += 1
                        continue

                    elif extention.lower() == ".bmp":
                        data["bmp_counter"] += 1
                        data["image_counter"] += 1
                        continue

                    elif extention.lower() == ".gif":
                        data["gif_counter"] += 1
                        data["image_counter"] += 1
                        continue

                    elif extention.lower() == ".png":
                        data["png_counter"] += 1
                        data["image_counter"] += 1
                        continue
# -------------------------------------------- document ----------------------------------------------------------------

                    elif extention.lower() == ".xlsx":
                        data["excel_counter"] += 1
                        data["document_counter"] += 1
                        continue

                    elif extention.lower() == ".rtf":
                        data["rtf_counter"] += 1
                        data["document_counter"] += 1
                        continue

                    elif extention.lower() == ".doc":
                        data["doc_counter"] += 1
                        data["document_counter"] += 1
                        continue
                    elif extention.lower() == ".pdf":
                        data["pdf_counter"] += 1
                        data["document_counter"] += 1
                        continue

                    else:
                        data["other_counter"] += 1
                        otherFiles.append(path.join(root, file))
    return otherFiles, data


def main():
    other_files = []
    try:
        input_argument = str(argv[1])
    except IndexError:
        print "Useage: " + path.basename(__file__) + " directory"
        return
    # check if path is valid
    if not path.isdir(input_argument):
        print "Not Valid directory"
        return
    else:
        print "Checking: " + input_argument,
        stdout.flush()

        other_files, data = get_data(input_argument)

        print "...done"
        # report
        report(data, other_files)


if __name__ == '__main__':
    main()
