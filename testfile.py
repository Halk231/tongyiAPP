import dashscope
dashscope.api_key="sk-00bbe4c439ce4203b62f22b9963a510a"
# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html
from http import HTTPStatus

from dashscope import Generation

def simple_sample():
    # model可以是模型列表任一模型
    response = Generation.call(model='llama2-13b-v2',
                               prompt='Hey, are you conscious? Can you talk to me?')
    if response.status_code == HTTPStatus.OK:
        print('Result is: %s' % response.output)
    else:
        print('Failed request_id: %s, status_code: %s, code: %s, message:%s' %
              (response.request_id, response.status_code, response.code,
               response.message))


if __name__ == '__main__':
    simple_sample()