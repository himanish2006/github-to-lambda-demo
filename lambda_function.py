import json

def cal_square(n):
    return n**2



def lambda_handler(event,context):
    print ("Event Data->",event)
    print("Trigger Received !!!")

    num =5
    res_square=cal_square(num)


    print("Square of {}".format(num),res_square)

    return {
        'statusCode' :200,
         'body':json.dumps('Bye Bye !!')
    }
    