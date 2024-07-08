import base64
import binascii
import sys

if sys.version_info[0] < 3:
    # Python 2
    activation_code = raw_input("请输入激活码(activation code)：")
else:
    # Python 3
    activation_code = input("请输入激活码(activation code)：")

# 将字符串中的"_"替换为"/"，并在结尾添加"="
modified_string = activation_code.replace("_", "/") + "="

# 对修改后的字符串进行Base64解码
decoded_data = base64.b64decode(modified_string).decode('utf-8')

# 将解码后的字符串解析为字典
decoded_dict = eval(decoded_data)

# 取出"seed"字段的值
seed_value = decoded_dict["token"]["seed"]

# 将提取出的值进行十六进制解码为二进制数据
binary_data = bytes.fromhex(seed_value)

# 对二进制数据进行Base32编码
secret = base64.b32encode(binary_data).decode()

# 打印编码后的结果
totp_url = 'otpauth://totp/TOTP?secret={}&issuer=宁盾&algorithm=SHA1&digits=6&period=60'.format(secret)
print(totp_url)