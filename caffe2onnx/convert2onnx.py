import argparse
from src.load_save_model import *
from src.caffe2onnx import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('CNP',help="caffe's caffemodel file path",nargs='?',default="./caffemodel/retina.prototxt")
    parser.add_argument('CMP',help="caffe's prototxt file path",nargs='?',default="./caffemodel/retina.caffemodel")
    parser.add_argument('ON',help="onnx model name",nargs='?',default="retina")
    parser.add_argument('OSP',help="onnx model file saved path",nargs='?',default="./onnxmodel/")
    args = parser.parse_args()

    NetPath = args.CNP
    ModelPath = args.CMP
    OnnxName = args.ON
    OnnxSavePath = args.OSP

    net,model = loadcaffemodel(NetPath,ModelPath)
    c2o = Caffe2Onnx(net,model,OnnxName)
    onnxmodel = c2o.createOnnxModel()
    saveonnxmodel(onnxmodel,OnnxSavePath+OnnxName)


if __name__ == '__main__':
    main()
