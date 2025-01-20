import json


def lambda_handler(event, context):
    try:

        num1 = float(event.get('num1', 0))
        num2 = float(event.get('num2', 0))
        operation = event.get('ope', '')

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ValueError("Division by zero is not allowed.")
            result = num1 / num2
        else:
            raise ValueError(f"Unsupported operation: {operation}")

        return {
            'statusCode': 200,
            'body': json.dumps({
                'result': result,
                'message': f'Successfully performed {operation} on {num1} and {num2}'
            })
        }

    except Exception as e:

        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': str(e),
                'message': 'Failed to perform the calculation'
            })
        }
