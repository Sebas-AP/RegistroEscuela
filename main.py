import flet as ft
from views.auth.login import get_login_view
from views.auth.register import get_register_view
from views.dashboard.menu import get_menu_view
from views.dashboard.agregar import get_agregar_view

def main(page: ft.Page):
    page.title = "Registro Escuela"
    # Handling v0.80+ vs older versions
    if hasattr(page, 'window'):
        page.window.width = 1000
        page.window.height = 700
    else:
        page.window_width = 1000
        page.window_height = 700
        
    page.theme_mode = ft.ThemeMode.DARK 
    
    def navigate(route):
        page.controls.clear()
        
        if route == "/login" or route == "/" or route == "":
            page.add(get_login_view(page))
        elif route == "/register":
            page.add(get_register_view(page))
        elif route == "/menu":
            page.add(get_menu_view(page))
        elif route == "/agregar":
            page.add(get_agregar_view(page))
        else:
            page.add(get_login_view(page))
            
        page.route = route
        page.update()

    # Override go method to use our custom navigator safely
    page.go = navigate
    
    # Load first view
    navigate("/login")

if __name__ == "__main__":
    import flet as ft
    if hasattr(ft, "run"):
        ft.run(main, assets_dir=".")
    else:
        ft.app(target=main, assets_dir=".")
