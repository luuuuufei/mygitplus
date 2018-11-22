
from PIL import Image
import os

def getGray(image_file):
    tmpls =[]
    for h in range(0, image_file.size[1]):  # h
        for w in range(0, image_file.size[0]):  # w
            tmpls.append(image_file.getpixel((w, h)))

    return tmpls


def getAvg(ls):  # 获取平均灰度值
    return sum(ls)/len(ls)

# 对比ab的相似度，
def getMH(a, b):
    dist = 0
    try:
        for i in range(0, len(a)):
            if a[i] == b[i]:
                dist = dist+1
        return dist
    except:
        return

def getImgHash(image_file):
    image_file =image_file.resize((12, 12))  # 重置图片大小为12px X 12px
    image_file =image_file.convert("L")  # 转256灰度图
    Grayls =getGray(image_file)  # 灰度集合
    avg =getAvg(Grayls)  # 灰度平均值
    bitls ='' # 接收获取0或1
    # 除去变宽1px遍历像素
    for h in range(1, image_file.size[1]-1):  # h
        for w in range(1, image_file.size[0]-1):  # w
            if image_file.getpixel((w, h))>=avg:# 像素的值比较平均值 大于记为1 小于记为0
                bitls =bitls + '1'
            else:
                bitls =bitls + '0'
    return bitls


def main():
    # 遍历本地文件夹中的小验证码
    files = os.listdir("./1kkkx")
    for image1 in files:
        # 异常捕捉，避免因删除相似的图片后，取不到时报错
        try:
            image_file1 = Image.open("./1kkkx/"+str(image1))
            a = getImgHash(image_file1)
        except:
            pass
        else:
            print('比对' + image1)
            # 遍历本地文件夹中的小验证码，与image1比对相似度
            files2 = os.listdir("./1kkkx")
            for image2 in files2:
                try:
                    image_filex = ("./1kkkx/"+str(image2))
                except:
                    pass
                else:
                    if image2 != image1:
                        image_file2 = Image.open(image_filex)
                        for i in range(4):
                            image_file2 = image_file2.rotate(90*i)
                            b = getImgHash(image_file2)
                            compare = getMH(a, b)
                            # print(image2, u'相似度', str(compare)+'%')
                            # 判断相似度大与80%的图片并删除
                            if compare > 80:
                                os.remove("./1kkkx/"+str(image2))
                                print('删除'"./1kkkx/"+str(image2))


if __name__ == '__main__':
    main()