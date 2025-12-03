#exemplo de como importar c macro e criar excel

import win32com.client as win32

# -----------------------------------
# INÍCIO – Abre o Excel
# -----------------------------------

excel = win32.Dispatch("Excel.Application")
excel.Visible = False   # coloque True se quiser ver a janela do Excel

# Cria um novo arquivo Excel
wb = excel.Workbooks.Add()

# Acessa o VBA Project
vb = wb.VBProject.VBComponents


# -----------------------------------
# IMPORTAR MÓDULOS .BAS MANUALMENTE
# Aqui você escolhe exatamente qual arquivo .bas importar
# -----------------------------------

# Exemplo 1 – importar arquivo .bas específico
vb.Import(r"C:\Users\Regina\Documents\macros\Modulo1.bas")

# Exemplo 2 – outro módulo opcional
vb.Import(r"C:\Users\Regina\Documents\macros\Validacoes.bas")

# Exemplo 3 – outro módulo opcional
vb.Import(r"C:\Users\Regina\Documents\macros\Calculos.bas")

# Basta repetir a linha acima e trocar o nome do arquivo
# Não é automático — você escolhe um a um.


# -----------------------------------
# SALVAR O ARQUIVO .XLSM
# -----------------------------------

wb.SaveAs(
    r"C:\Users\Regina\Documents\ArquivoFinalComMacros.xlsm",
    FileFormat=52  # 52 = XLSM (com macro)
)


# -----------------------------------
# FINALIZA
# -----------------------------------

wb.Close()
excel.Quit()
