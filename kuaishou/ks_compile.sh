# bin/bash
for FILE in $(find . -name "*.proto"); # 找到 proto 目录下以 proto 后缀结尾的文件，然后逐个编译
do
  python -m grpc_tools.protoc -I . --python_out=.  $FILE
  echo "python -m grpc_tools.protoc -I . --python_out=.  $FILE";
done