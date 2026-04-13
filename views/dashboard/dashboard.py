import flet as ft
from components.sidebar import get_sidebar
from core.database import get_supabase_client

def get_dashboard_view(page: ft.Page):
    supabase = get_supabase_client()
    
    # State
    alumnos_data = []
    
    # UI Elements
    search_input = ft.TextField(
        hint_text="Buscar alumno...", 
        prefix_icon=ft.Icons.SEARCH,
        expand=True,
        border_radius=20,
        height=40,
        content_padding=10
    )
    
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Matrícula")),
            ft.DataColumn(ft.Text("Grado"))
        ],
        rows=[],
        expand=True
    )
    
    def load_data():
        if not supabase:
            return
        
        try:
            # Query the 'alumnos' table
            response = supabase.table("alumnos").select("*").execute()
            alumnos_data = response.data
            
            # Update data table rows
            data_table.rows.clear()
            for alu in alumnos_data:
                data_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(alu.get("id", "")))),
                            ft.DataCell(ft.Text(str(alu.get("nombre", "")))),
                            ft.DataCell(ft.Text(str(alu.get("matricula", "")))),
                            ft.DataCell(ft.Text(str(alu.get("grado", "")))),
                        ]
                    )
                )
            page.update()
        except Exception as e:
            print("Error fetching alumnos:", e)
            
    # Top bar
    top_bar = ft.Container(
        padding=10,
        margin=ft.margin.only(bottom=20),
        border_radius=10,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        content=ft.Row(
            controls=[
                search_input,
                ft.ElevatedButton("Nuevo Registro", icon=ft.Icons.ADD, bgcolor=ft.Colors.BLUE_400, color=ft.Colors.WHITE)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    main_content = ft.Container(
        expand=True,
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text("Panel de Alumnos", size=28, weight=ft.FontWeight.BOLD),
                top_bar,
                ft.Container(
                    expand=True,
                    padding=10,
                    border=ft.border.all(1, ft.Colors.OUTLINE_VARIANT),
                    border_radius=10,
                    content=ft.ListView(
                        expand=True,
                        controls=[data_table]
                    )
                )
            ]
        )
    )

    # layout
    layout = ft.Row(
        expand=True,
        controls=[
            get_sidebar(page, active_route="/dashboard"),
            main_content
        ]
    )
    
    # Load data synchronously
    load_data()

    return layout
