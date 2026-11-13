import json


def main():
    test_num = int(input('Enter the number of wanted tests: '))
    auto_name =  input('Name tests automatically (default: no)? (y/n): ') == 'y'

    data = {"tests": []}
    for i in range(test_num):
        if not auto_name:
            test_name = input(f'Enter test {i+1} name: ')
        else:
            test_name = f'test {i+1}'

        test_in = input(f'Enter test input:').replace('\\n', '\n')
        test_out = input(f'Enter test output:').replace('\\n', '\n')
        print('')
        data['tests'].append({"name": test_name ,"input": test_in, "output": test_out})

    with open('student_tests.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    main()