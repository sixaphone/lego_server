import subprocess


class CLI:

  def run_command(self, command):
    try:
      chunked_command = None

      if isinstance(command, str):
        chunked_command = command.split()

      if isinstance(command, list):
        chunked_command = command

      if not chunked_command:
        raise Exception('Invalid command.')

      proccess = subprocess.Popen(chunked_command,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)

      stdout, stderr = proccess.communicate()

      if stderr:
        raise Exception('Error on command ' + ' '.join(chunked_command))

      return stdout
    except Exception as e:
        print(str(e))
        exit()
