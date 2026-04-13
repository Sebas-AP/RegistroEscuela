import flet as ft

def get_sidebar(page: ft.Page, active_route: str = "/dashboard"):
    
    def navigate(e, route):
        if page.route != route:
            page.go(route)
            
    return ft.Container(
        width=250,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        border_radius=10,
        padding=15,
        content=ft.Column(
            controls=[
                ft.Row(
                    [
                        ft.Icon(ft.Icons.SCHOOL, size=30, color=ft.Colors.BLUE_400),
                        ft.Text("Escuela App", size=20, weight=ft.FontWeight.BOLD)
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                ft.Divider(height=20, color=ft.Colors.OUTLINE_VARIANT),
                # User Profile Placeholder
                ft.Row(
                    [
                        ft.CircleAvatar(
                            content=ft.Icon(ft.Icons.PERSON)
                        ),
                        ft.Text("Usuario", weight=ft.FontWeight.W_500)
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                ft.Divider(height=20, color=ft.Colors.OUTLINE_VARIANT),
                # Navigation Items
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.DASHBOARD, color=ft.Colors.BLUE_400 if active_route == "/dashboard" else None),
                    title=ft.Text("Alumnos", color=ft.Colors.BLUE_400 if active_route == "/dashboard" else None),
                    on_click=lambda e: navigate(e, "/dashboard"),
                    selected=active_route == "/dashboard"
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.SETTINGS, color=ft.Colors.BLUE_400 if active_route == "/settings" else None),
                    title=ft.Text("Configuración", color=ft.Colors.BLUE_400 if active_route == "/settings" else None),
                    # on_click=lambda e: navigate(e, "/settings"),
                    selected=active_route == "/settings"
                ),
                ft.Container(expand=True), # Spacer to push logout to bottom
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.LOGOUT, color=ft.Colors.RED_400),
                    title=ft.Text("Cerrar Sesión", color=ft.Colors.RED_400),
                    on_click=lambda e: navigate(e, "/login")
                ),
            ]
        )
    )
