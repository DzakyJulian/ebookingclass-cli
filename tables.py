from prettytable import PrettyTable

alat_table = PrettyTable()
alat_table.field_names = ["id", "kode_kelas", "alat", "keterangan"]

kelas = [
    ["20.4B.04.002", "Kamis 12 November 2024, 12:35", "Tersedia"],
    ["20.4E.02.006", "Rabu 12 November 2024, 12:35", "Penuh"]
]

alat = [
    ["1", "20.4B.04.002", "Infocus", "Tersedia"],
    ["2", "20.4B.04.004", "Spidol", "Tersedia"],
    ["3", "20.4B.04.006", "Remot AC", "Tidak Tersedia"]
]

alat_table.add_rows(alat)