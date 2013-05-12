import cv
import sys
 
HAAR_CASCADE_PATH = '/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml'

storage = cv.CreateMemStorage()
cascade = cv.Load(HAAR_CASCADE_PATH)
 
def detect_faces(image):
    faces = []
    detected = cv.HaarDetectObjects(image, cascade, storage, 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))
    if detected:
        for (x,y,w,h),n in detected:
            faces.append((x,y,w,h))
    return faces

def face_blit(src, dst):
    #TODO handle errors
    # extract the face from the source
    src_face_coords = detect_faces(src)[0]
    src_face = cv.GetSubRect(src, src_face_coords)

    # extract the face from the destination
    dst_face_coords = detect_faces(dst)[0]
    dst_face = cv.GetSubRect(dst, dst_face_coords)

    # scale the source face to the size of the destination face
    src_face_scale = cv.CreateMat(dst_face_coords[2], dst_face_coords[3], cv.CV_8UC3)
    cv.Resize(src_face, src_face_scale)

    # copy the source face onto the destination face
    # this updates dst
    cv.Copy(src_face_scale, dst_face)
    return dst
 
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print 'usage: {} [src] [dst] [output]'.format(sys.argv[0])
        sys.exit(1)
    src_image = cv.LoadImageM(sys.argv[1])
    dst_image = cv.LoadImageM(sys.argv[2])
    dst_image = face_blit(src_image, dst_image)
    cv.SaveImage(sys.argv[3], dst_image)
