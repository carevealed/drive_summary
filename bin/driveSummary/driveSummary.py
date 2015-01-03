#!/usr/bin/python
from sys import argv, stdout, stderr
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
    if data["audio_counter"] != 0:
        print "\n=================== AUDIO FILES ==================="
        if data["mp3_counter"] != 0:
            print "The number of mp3 files are: \t\t" + str(data["mp3_counter"])

        if data["m4a_counter"] != 0:
            print "The number of m4a files are: \t\t" + str(data["m4a_counter"])

        if data["mpc_counter"] != 0:
            print "The number of musepack files are: \t" + str(data["mpc_counter"])

        if data["wave_counter"] != 0:
            print "The number of wav files are: \t\t" + str(data["wave_counter"])

        if data["flac_counter"] != 0:
            print "The number of flac files are: \t\t" + str(data["flac_counter"])

        if data["ogg_counter"] != 0:
            print "The number of ogg files are: \t\t" + str(data["ogg_counter"])

        if data["wma_counter"] != 0:
            print "The number of wma files are: \t\t" + str(data["wma_counter"])

    if data["video_counter"] != 0:
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

    if data["image_counter"] != 0:
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

    if data["document_counter"] != 0:
        print "\n================= DOCUMENT FILES =================="
        if data["excel_counter"] != 0:
            print "The number of excel files are: \t\t" + str(data["excel_counter"])

        if data["rtf_counter"] != 0:
            print "The number of rich text \"rtf\" files are:" + str(data["rtf_counter"])

        if data["txt_counter"] != 0:
            print "The number of txt files are:\t\t" + str(data["txt_counter"])

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
        "m4a_counter": 0,
        "mpc_counter": 0,
        "flac_counter": 0,
        "wma_counter": 0,
        "ogg_counter": 0,
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
        "txt_counter": 0,
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
    others_file_types = []
    if path.isdir(input_argument):
        for root, dir, files in walk(input_argument):
            for file in files:
                if path.isfile(path.join(root, file)):
                    file_name, extension = path.splitext(file)
                    data["total_counter"] += 1
                    data["total_file_size"] += path.getsize(path.join(root, file))
                    if extension == ".md5":
                        data["md5_counter"] += 1
                        continue

# ---------------------------------------------- audio -----------------------------------------------------------------

                    elif extension.lower() == ".flac":
                        data["flac_counter"] += 1
                        data["audio_counter"] += 1
                        continue

                    elif extension.lower() == ".m4a":
                        data["m4a_counter"] += 1
                        data["audio_counter"] += 1
                        continue

                    elif extension.lower() == ".mp3":
                        data["mp3_counter"] += 1
                        data["audio_counter"] += 1
                        continue

                    elif extension.lower() == ".mpc":
                        data["mpc_counter"] += 1
                        data["audio_counter"] += 1
                        continue

                    elif extension.lower() == ".ogg":
                        data["ogg_counter"] += 1
                        data["audio_counter"] += 1
                        continue

                    elif extension.lower() == ".wav":
                        data["wave_counter"] += 1
                        data["audio_counter"] += 1
                        continue

                    elif extension.lower() == ".wma":
                        data["wma_counter"] += 1
                        data["audio_counter"] += 1
                        continue
# --------------------------------------------- video -----------------------------------------------------------------
                    elif extension.lower() == ".avi":
                        data["avi_counter"] += 1
                        data["video_counter"] += 1
                        continue

                    elif extension.lower() == ".dv":
                        data["dv_counter"] += 1
                        data["video_counter"] += 1
                        continue

                    elif extension.lower() == ".m4v":
                        data["m4v_counter"] += 1
                        data["video_counter"] += 1
                        continue

                    elif extension.lower() == ".mov":
                        data["mov_counter"] += 1
                        data["video_counter"] += 1
                        continue

                    elif extension.lower() == ".mp4":
                        data["mp4_counter"] += 1
                        data["video_counter"] += 1
                        continue
# ---------------------------------------------- image -----------------------------------------------------------------
                    elif extension.lower() == ".bmp":
                        data["bmp_counter"] += 1
                        data["image_counter"] += 1
                        continue

                    elif extension.lower() == ".gif":
                        data["gif_counter"] += 1
                        data["image_counter"] += 1
                        continue

                    elif extension.lower() == ".jpg" or extension.lower() == ".jpeg":
                        data["jpeg_counter"] += 1
                        data["image_counter"] += 1
                        continue

                    elif extension.lower() == ".png":
                        data["png_counter"] += 1
                        data["image_counter"] += 1
                        continue

                    elif extension.lower() == ".tif" or extension.lower() == ".tiff":
                        data["tiff_counter"] += 1
                        data["image_counter"] += 1
                        continue
# -------------------------------------------- document ----------------------------------------------------------------

                    elif extension.lower() == ".xlsx":
                        data["excel_counter"] += 1
                        data["document_counter"] += 1
                        continue

                    elif extension.lower() == ".txt":
                        data["txt_counter"] += 1
                        data["document_counter"] += 1
                        continue

                    elif extension.lower() == ".rtf":
                        data["rtf_counter"] += 1
                        data["document_counter"] += 1
                        continue

                    elif extension.lower() == ".doc":
                        data["doc_counter"] += 1
                        data["document_counter"] += 1
                        continue

                    elif extension.lower() == ".pdf":
                        data["pdf_counter"] += 1
                        data["document_counter"] += 1
                        continue

                    else:
                        data["other_counter"] += 1
                        others_file_types.append(path.join(root, file))
    return others_file_types, data


# def main():
#     other_files = []
#     try:
#         input_argument = str(argv[1])
#     except IndexError:
#         print "Usage: " + path.basename(__file__) + " directory"
#         return
#     # check if path is valid
#     if not path.isdir(input_argument):
#         stderr.write(str("\"" + input_argument + "\"is not a valid directory"))
#         return
#     else:
#         print "Checking: " + input_argument,
#         stdout.flush()
#
#         other_files, data = get_data(input_argument)
#
#         print "...done"
#
#         report(data, other_files) # Generate a report



if __name__ == '__main__':
    print "cannot run module"
