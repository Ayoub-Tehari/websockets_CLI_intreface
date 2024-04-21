
import subprocess

def run_program(program, input_data):
  """
  Runs the specified program with the provided input data.

  Args:
      program: The path to the program executable.
      input_data: The data to be passed as input to the program.

  Returns:
      A tuple containing the program's output (stdout) and any errors (stderr).
  """
  process = subprocess.Popen([program], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  output, error = process.communicate(input=input_data)
  return output.decode('utf-8'), error.decode('utf-8')

# Exemple d'utilisation (à appeler depuis l'API Flask)
def exec_cmd_interactive(command, args=[]):
  return run_program(command, args)

def exec_cat_on_file (raw_content) :
  return exec_cmd_interactive('cat', raw_content.encode())