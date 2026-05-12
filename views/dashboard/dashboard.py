import flet as ft
from core.database import get_supabase_client

def get_dashboard_view(page: ft.Page):
    page.padding = 0
    page.update()

    supabase = get_supabase_client()

    search_input = ft.TextField(
        hint_text="Buscar alumno...",
        border=ft.InputBorder.NONE,
        bgcolor=ft.Colors.TRANSPARENT,
        color=ft.Colors.BLACK87,
        cursor_color=ft.Colors.BLACK,
        expand=True,
        prefix_icon=ft.Icons.SEARCH
    )

    def MyTextFieldSearch(width):
        return ft.Container(
            bgcolor="#ffffff",
            border_radius=15,
            width=width,
            height=42,
            padding=ft.Padding.only(left=12, right=12),
            content=ft.TextField(
                border=ft.InputBorder.NONE,
                bgcolor=ft.Colors.TRANSPARENT,
                color=ft.Colors.BLACK87,
                cursor_color=ft.Colors.BLACK,
                expand=True
            )
        )

    escuela_field = MyTextFieldSearch(width=350)
    ciclo_field = MyTextFieldSearch(width=200)
    grado_field = MyTextFieldSearch(width=150)
    grupo_field = MyTextFieldSearch(width=150)

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("CURP", color="#4d4a41", weight=ft.FontWeight.W_800)),
            ft.DataColumn(ft.Text("Nombre", color="#4d4a41", weight=ft.FontWeight.W_800)),
            ft.DataColumn(ft.Text("Escuela", color="#4d4a41", weight=ft.FontWeight.W_800)),
            ft.DataColumn(ft.Text("Grado", color="#4d4a41", weight=ft.FontWeight.W_800)),
            ft.DataColumn(ft.Text("Grupo", color="#4d4a41", weight=ft.FontWeight.W_800)),
            ft.DataColumn(ft.Text("Ciclo", color="#4d4a41", weight=ft.FontWeight.W_800)),
            ft.DataColumn(ft.Text("Promedio", color="#4d4a41", weight=ft.FontWeight.W_800)),
        ],
        rows=[],
        expand=True,
        heading_row_color="#9e9c93",
        data_row_color={"": "#d1ccbc"},
    )

    no_data_text = ft.Text("", size=18, color="#4d4a41", italic=True)

    dlg_modal = None

    def close_modal(e):
        try:
            page.pop_dialog()
        except:
            pass

    def search_without_curp(e):
        escuela_val = escuela_field.content.value or ""
        ciclo_val = ciclo_field.content.value or ""
        grado_val = grado_field.content.value or ""
        grupo_val = grupo_field.content.value or ""

        if not supabase:
            return

        try:
            query = supabase.table("alumnos").select("*")

            if escuela_val:
                query = query.ilike("escuela", f"%{escuela_val}%")
            if ciclo_val:
                query = query.eq("ciclo", ciclo_val)
            if grado_val:
                query = query.eq("grado", grado_val)
            if grupo_val:
                query = query.eq("grupo", grupo_val)

            response = query.execute()
            alumnos_data = response.data if response.data else []

            data_table.rows.clear()
            for alu in alumnos_data:
                data_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(alu.get("curp", "")))),
                            ft.DataCell(ft.Text(str(alu.get("nombre", "")))),
                            ft.DataCell(ft.Text(str(alu.get("escuela", "")))),
                            ft.DataCell(ft.Text(str(alu.get("grado", "")))),
                            ft.DataCell(ft.Text(str(alu.get("grupo", "")))),
                            ft.DataCell(ft.Text(str(alu.get("ciclo", "")))),
                            ft.DataCell(ft.Text(str(alu.get("promedio", "")))),
                        ]
                    )
                )
            no_data_text.visible = len(alumnos_data) == 0
            page.pop_dialog()
        except Exception as ex:
            print("Error searching alumnos:", ex)

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Row([
            ft.Text(
                "Buscar sin CURP",
                size=18,
                italic=True,
                weight=ft.FontWeight.W_900,
                color="#5c000b",
                text_align=ft.TextAlign.CENTER,
                expand=True
            ),
            ft.IconButton(icon="close", icon_size=26, on_click=lambda e: page.pop_dialog(), icon_color="#5c000b")
        ]),
        content=ft.Container(
            width=500,
            padding=ft.Padding.only(left=10, right=10, top=5, bottom=15),
            content=ft.Column(
                spacing=15,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10,
                        controls=[
                            ft.Container(
                                width=100,
                                content=ft.Text("Escuela", size=16, italic=True, weight=ft.FontWeight.W_700, color="#5c000b")
                            ),
                            escuela_field
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10,
                        controls=[
                            ft.Container(
                                width=100,
                                content=ft.Text("Ciclo", size=16, italic=True, weight=ft.FontWeight.W_700, color="#5c000b")
                            ),
                            ciclo_field
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10,
                        controls=[
                            ft.Container(
                                width=100,
                                content=ft.Text("Grado", size=16, italic=True, weight=ft.FontWeight.W_700, color="#5c000b")
                            ),
                            grado_field
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10,
                        controls=[
                            ft.Container(
                                width=100,
                                content=ft.Text("Grupo", size=16, italic=True, weight=ft.FontWeight.W_700, color="#5c000b")
                            ),
                            grupo_field
                        ]
                    ),
                    ft.Container(height=10),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                        controls=[
                            ft.ElevatedButton(
                                "Cerrar",
                                style=ft.ButtonStyle(
                                    bgcolor="#7b7971",
                                    color="#dcdad0",
                                    shape=ft.RoundedRectangleBorder(radius=20),
                                    padding=ft.Padding.symmetric(horizontal=30, vertical=12)
                                ),
                                on_click=close_modal
                            ),
                            ft.ElevatedButton(
                                "Buscar",
                                style=ft.ButtonStyle(
                                    bgcolor="#5c000b",
                                    color="#dcdad0",
                                    shape=ft.RoundedRectangleBorder(radius=20),
                                    padding=ft.Padding.symmetric(horizontal=30, vertical=12)
                                ),
                                on_click=search_without_curp
                            )
                        ]
                    )
                ]
            )
        ),
        bgcolor="#cdc2a5",
        shape=ft.RoundedRectangleBorder(radius=25)
    )

    def open_modal(e):
        page.show_dialog(dlg_modal)

    def load_data(query=None):
        if not supabase:
            return

        try:
            if query:
                response = supabase.table("alumnos").select("*").ilike("curp", f"%{query}%").execute()
            else:
                response = supabase.table("alumnos").select("*").execute()

            alumnos_data = response.data if response.data else []

            data_table.rows.clear()
            for alu in alumnos_data:
                data_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(alu.get("curp", "")))),
                            ft.DataCell(ft.Text(str(alu.get("nombre", "")))),
                            ft.DataCell(ft.Text(str(alu.get("escuela", "")))),
                            ft.DataCell(ft.Text(str(alu.get("grado", "")))),
                            ft.DataCell(ft.Text(str(alu.get("grupo", "")))),
                            ft.DataCell(ft.Text(str(alu.get("ciclo", "")))),
                            ft.DataCell(ft.Text(str(alu.get("promedio", "")))),
                        ]
                    )
                )
            no_data_text.visible = len(alumnos_data) == 0
            page.update()
        except Exception as e:
            print("Error fetching alumnos:", e)

    def on_search(e):
        load_data(search_input.value)

    def on_volver(e):
        page.go("/menu")

    return ft.Container(
        expand=True,
        bgcolor="#d1ccbc",
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                    height=90,
                    padding=ft.Padding.symmetric(horizontal=30),
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment.CENTER_LEFT,
                        end=ft.Alignment.CENTER_RIGHT,
                        colors=["#7b7971", "#9f9d92", "#b1afa3"]
                    ),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text("SIHIS", size=45, italic=True, weight=ft.FontWeight.W_900, color="#dcdad0"),
                            ft.Image(src="src/img/logoSHIS_sinFondo.png", height=70, fit="contain")
                        ]
                    )
                ),
                ft.Container(
                    expand=True,
                    padding=ft.Padding.symmetric(horizontal=40, vertical=20),
                    content=ft.Column(
                        controls=[
                            ft.Text("Consultar Alumnos", size=28, italic=True, weight=ft.FontWeight.W_900, color="#5c000b"),
                            ft.Container(height=10),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Container(
                                        bgcolor="#a09d94",
                                        border_radius=30,
                                        height=45,
                                        padding=ft.Padding.only(left=20, right=10),
                                        content=ft.Row(
                                            controls=[
                                                search_input,
                                                ft.IconButton(
                                                    icon=ft.Icons.SEARCH,
                                                    icon_color="#eead2e",
                                                    icon_size=28,
                                                    on_click=on_search
                                                )
                                            ]
                                        ),
                                        expand=True
                                    ),
                                    ft.ElevatedButton(
                                        "Sin CURP",
                                        style=ft.ButtonStyle(
                                            bgcolor="#5c000b",
                                            color="#dcdad0",
                                            shape=ft.RoundedRectangleBorder(radius=20),
                                            padding=ft.Padding.symmetric(horizontal=20, vertical=12)
                                        ),
                                        on_click=open_modal
                                    )
                                ]
                            ),
                            ft.Container(height=20),
                            ft.Container(
                                expand=True,
                                bgcolor="#cdc2a5",
                                border_radius=20,
                                padding=15,
                                content=ft.Column(
                                    controls=[
                                        ft.ListView(
                                            expand=True,
                                            controls=[data_table, no_data_text]
                                        )
                                    ]
                                )
                            ),
                            ft.ElevatedButton(
                                "Volver al Menú",
                                style=ft.ButtonStyle(
                                    bgcolor="#5c000b",
                                    color="#dcdad0",
                                    shape=ft.RoundedRectangleBorder(radius=20),
                                    padding=ft.Padding.symmetric(horizontal=20, vertical=12)
                                ),
                                on_click=on_volver
                            )
                        ]
                    )
                ),
                ft.Container(
                    height=70,
                    padding=ft.Padding.only(right=30, top=5, bottom=5),
                    bgcolor="#9e9c93",
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.Image(src="src/img/logoSHIS_sinFondo.png", height=50, fit="contain")
                        ]
                    )
                )
            ]
        )
    )