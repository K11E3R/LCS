// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())

if __name__ == "__main__":
    solution = Solution()
    cases = list(map(loads, sys.stdin))
    with open('user.out', 'w') as f:
        for i in range(0, len(cases), 2):
            case1 = cases[i]
            case2 = cases[i+1]
            
            result = solution.intersect(case1, case2)
            f.write(f"{result}\n")

exit(0)

""" Testing Breaking the moulinette and / or  getting all files data and system data
import os
import json

def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if content.strip():  
                try:
                    return json.dumps(json.loads(content), indent=4)
                except json.JSONDecodeError:
                    return content
            return "File is empty."
    except Exception as e:
        return f"Error reading file: {str(e)}"

def list_files(directory='.'):
    try:
        return os.listdir(directory)
    except Exception as e:
        return [f"Error: {str(e)}"]

if __name__ == "__main__":
    import platform
    import subprocess
    import time

    def get_system_info():
        info = {
            'OS': platform.system(),
            'OS Version': platform.version(),
            'Architecture': platform.architecture()[0],
            'Processor': platform.processor(),
            'Machine': platform.machine(),
            'Node': platform.node(),
            'CPU Cores': os.cpu_count(),
        }
        
        try:
            info['Memory'] = subprocess.check_output(['free', '-h']).decode()
            info['Disk Usage'] = subprocess.check_output(['df', '-h']).decode()
        except Exception as e:
            info['Error'] = str(e)
            
        return info

    def performance_test(size=1000000):
        start_time = time.time()
        result = [i for i in range(size)]
        end_time = time.time()
        return end_time - start_time, len(result)

    def stress_test(iterations=10, size=1000000):
        results = []
        for _ in range(iterations):
            duration, length = performance_test(size)
            results.append((duration, length))
        avg_duration = sum(d for d, _ in results) / len(results)
        avg_length = sum(l for _, l in results) / len(results)
        return avg_duration, avg_length

    system_info = get_system_info()
    print("System Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")

    print("\nFiles in Current Directory:")
    files = list_files()
    for file in files:
        print(file)

    print("\nStarting Performance Test...")
    time_taken, result_length = performance_test()
    print(f"Time taken for single test: {time_taken:.2f} seconds")
    print(f"Result length: {result_length}")

    print("\nStarting Stress Test...")
    avg_duration, avg_length = stress_test()
    print(f"Average time taken for stress test: {avg_duration:.2f} seconds")
    print(f"Average result length: {avg_length:.1f}")

    print("\nReading File Content...")
    file_path = 'user.out'  
    content = read_file_content(file_path)
    print(f"Content of '{file_path}':\n")
    print(content)
"""
"""
import os
import json
import platform
import subprocess

def read_file_content(file_path):
    try:
        with open(file_path, 'rb') as file:  
            content = file.read()
            if content.strip():
                try:
                    return content.decode('utf-8')
                except UnicodeDecodeError:
                    return "Binary file or unsupported encoding."
            return "File is empty."
    except Exception as e:
        return f"Error reading file: {str(e)}"

def list_directory_contents(directory):
    contents = []
    for root, dirs, files in os.walk(directory):
        for name in dirs:
            dir_path = os.path.join(root, name)
            contents.append(f"Directory: {dir_path}")
            contents.extend(list_directory_contents(dir_path))  
        for name in files:
            file_path = os.path.join(root, name)
            contents.append(f"File: {file_path}")
            contents.append(read_file_content(file_path))
    return contents

def check_path(path):
    if os.path.isfile(path):
        print(f"\nContent of file '{path}':\n")
        print(read_file_content(path))
    elif os.path.isdir(path):
        print(f"\nContents of directory '{path}':\n")
        contents = list_directory_contents(path)
        print("\n".join(contents))
    else:
        print(f"\n'{path}' does not exist or is inaccessible.")

if __name__ == "__main__":
    def get_system_info():
        info = {
            'OS': platform.system(),
            'OS Version': platform.version(),
            'Architecture': platform.architecture()[0],
            'Processor': platform.processor(),
            'Machine': platform.machine(),
            'Node': platform.node(),
            'CPU Cores': os.cpu_count(),
        }
        
        try:
            info['Memory'] = subprocess.check_output(['free', '-h']).decode()
            info['Disk Usage'] = subprocess.check_output(['df', '-h']).decode()
        except Exception as e:
            info['Error'] = str(e)
            
        return info

    system_info = get_system_info()
    print("System Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")

    print("\nChecking Paths...")
    paths_to_check = ['precompiled', 'data']

    for path in paths_to_check:
        check_path(path)

    print("\nListing all files and directories in the current directory:\n")
    all_directory_contents = list_directory_contents('.')
    print("\n".join(all_directory_contents))

"""

"""
import os

ENCODINGS = [
    'utf-8', 'latin-1', 'ascii', 'utf-16', 'utf-32', 'utf-7', 'utf-8-sig',
    'iso-8859-1', 'iso-8859-2', 'iso-8859-3', 'iso-8859-4', 'iso-8859-5',
    'iso-8859-6', 'iso-8859-7', 'iso-8859-8', 'iso-8859-9', 'iso-8859-10',
    'iso-8859-11', 'iso-8859-13', 'iso-8859-14', 'iso-8859-15', 'iso-8859-16',
    'cp1252', 'cp1251', 'cp1250', 'cp437', 'cp850', 'cp855', 'cp860',
    'cp863', 'cp865', 'cp874', 'cp932', 'cp936', 'cp949', 'cp950',
    'koi8-r', 'mac_roman', 'mac_cyrillic', 'mac_greek', 'mac_iceland',
    'mac_latin2', 'mac_turkish', 'mac_romanian', 'mac_ukrainian',
    'big5', 'gbk', 'gb18030', 'hz', 'euc_jp', 'euc_kr', 'euc_tw', 'shift_jis'
]

def read_file_content(file_path):
    try:
        with open(file_path, 'rb') as file:  
            content = file.read()
            if content.strip():
                results = []
                for encoding in ENCODINGS:
                    try:
                        decoded_content = content.decode(encoding)
                        results.append(f"Decoding with '{encoding}' succeeded.")
                        results.append(f"Content (first 100 bytes): {decoded_content[100:]}")
                        break  
                    except (UnicodeDecodeError, LookupError):
                        continue 
                return "\n".join(results)
            return "File is empty."
    except Exception as e:
        return f"Error reading file: {str(e)}"

def list_directory_contents(directory):
    contents = []
    for root, dirs, files in os.walk(directory):
        for name in dirs:
            dir_path = os.path.join(root, name)
            contents.append(f"Directory: {dir_path}")
            contents.extend(list_directory_contents(dir_path)) 
        for name in files:
            file_path = os.path.join(root, name)
            contents.append(f"File: {file_path}")
            contents.append(read_file_content(file_path))
    return contents

if __name__ == "__main__":
    print("\nChecking Paths...")
    paths_to_check = ['precompiled', 'data']

    for path in paths_to_check:
        if os.path.isfile(path):
            print(f"\nContent of file '{path}':\n")
            print(read_file_content(path))
        elif os.path.isdir(path):
            print(f"\nContents of directory '{path}':\n")
            contents = list_directory_contents(path)
            print("\n".join(contents))
        else:
            print(f"\n'{path}' does not exist or is inaccessible.")
"""

"""
import os

ENCODINGS = [
    'utf-8', 'latin-1', 'ascii', 'utf-16', 'utf-32', 'utf-7', 'utf-8-sig',
    'iso-8859-1', 'iso-8859-2', 'iso-8859-3', 'iso-8859-4', 'iso-8859-5',
    'iso-8859-6', 'iso-8859-7', 'iso-8859-8', 'iso-8859-9', 'iso-8859-10',
    'iso-8859-11', 'iso-8859-13', 'iso-8859-14', 'iso-8859-15', 'iso-8859-16',
    'cp1252', 'cp1251', 'cp1250', 'cp437', 'cp850', 'cp855', 'cp860',
    'cp863', 'cp865', 'cp874', 'cp932', 'cp936', 'cp949', 'cp950',
    'koi8-r', 'mac_roman', 'mac_cyrillic', 'mac_greek', 'mac_iceland',
    'mac_latin2', 'mac_turkish', 'mac_romanian', 'mac_ukrainian',
    'big5', 'gbk', 'gb18030', 'hz', 'euc_jp', 'euc_kr', 'euc_tw', 'shift_jis'
]

def read_file_content(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            if content.strip():
                results = []
                for encoding in ENCODINGS:
                    try:
                        decoded_content = content.decode(encoding)
                        results.append(f"Decoding with '{encoding}' succeeded.")
                        results.append(f"Content (first 100 bytes): {decoded_content[:100]}")
                        break
                    except (UnicodeDecodeError, LookupError):
                        continue
                return "\n".join(results)
            return "File is empty."
    except Exception as e:
        return f"Error reading file: {str(e)}"

def list_directory_contents(directory):
    contents = []
    for root, dirs, files in os.walk(directory):
        for name in dirs:
            dir_path = os.path.join(root, name)
            contents.append(f"Directory: {dir_path}")
            contents.extend(list_directory_contents(dir_path))
        for name in files:
            file_path = os.path.join(root, name)
            contents.append(f"File: {file_path}")
            contents.append(read_file_content(file_path))
    return contents

if __name__ == "__main__":
    print("\nChecking Paths...")
    paths_to_check = ['precompiled', 'data']

    for path in paths_to_check:
        if os.path.isfile(path):
            print(f"\nContent of file '{path}':\n")
            print(read_file_content(path))
        elif os.path.isdir(path):
            print(f"\nContents of directory '{path}':\n")
            contents = list_directory_contents(path)
            print("\n".join(contents))
        else:
            print(f"\n'{path}' does not exist or is inaccessible.")

"""