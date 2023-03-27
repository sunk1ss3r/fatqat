import argparse, os, sys
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument("--mode", help="Choose a program mode: {gcs, imgproc, gcs+imgproc}", required=True)
parser.add_argument("--cam_src", help="Camera video feed source")
parser.add_argument("--ir_cam_src", help="IR camera video feed source")
parser.add_argument("--app", help="Image application")

args = parser.parse_args()

if args.mode == "gcs_only":
    print(colored("[i] Ground Control Station only", 'green'))

elif args.mode == "imgproc":
    if not (args.cam_src and args.ir_cam_src and args.app):
        parser.error("imgProc mode requires --cam_src,--ir_cam_src, and --app arguments")
    
    # Do something with the camera video feed sources
    print(colored("[i] Set video feed source (cam): %s" % args.cam_src, 'blue'))
    print(colored("[i] Set infrared video feed source (ir_cam): %s" % args.ir_cam_src, 'blue'))
    print(colored("[i] Name of the image processing application: %s" % args.app, 'blue'))

    os.system(f"python3 modules/img_proc_apps/{args.app} --cam_src {args.cam_src} --ir_cam_src {args.ir_cam_src}")

else:
    print(f"Mode {args.mode} is not supported.")
