import gradio as gr

from src.webui.components.agent_settings_tab import create_agent_settings_tab
from src.webui.components.browser_settings_tab import create_browser_settings_tab
from src.webui.components.browser_use_agent_tab import create_browser_use_agent_tab
from src.webui.components.deep_research_agent_tab import create_deep_research_agent_tab
from src.webui.webui_manager import WebuiManager

theme_map = {
    "Default": gr.themes.Default(),
    "Soft": gr.themes.Soft(),
    "Monochrome": gr.themes.Monochrome(),
    "Glass": gr.themes.Glass(),
    "Origin": gr.themes.Origin(),
    "Citrus": gr.themes.Citrus(),
    "Ocean": gr.themes.Ocean(),
    "Base": gr.themes.Base(),
}


def create_ui(theme_name="Ocean"):
    css = """
    .gradio-container {
        width: 70vw !important; 
        max-width: 70% !important; 
        margin-left: auto !important;
        margin-right: auto !important;
        padding-top: 10px !important;
    }
    .header-text {
        text-align: center;
        margin-bottom: 20px;
    }
    .tab-header-text {
        text-align: center;
    }
    .theme-section {
        margin-bottom: 10px;
        padding: 15px;
        border-radius: 10px;
    }
    """

    # dark mode in default
    js_func = """
    function refresh() {
        const url = new URL(window.location);

        if (url.searchParams.get('__theme') !== 'dark') {
            url.searchParams.set('__theme', 'dark');
            window.location.href = url.href;
        }
    }
    """

    ui_manager = WebuiManager()

    with gr.Blocks(
        title="The Browser",
        theme=theme_map[theme_name],
        css=css,
        # js=js_func,
    ) as demo:
        with gr.Row():
            gr.Markdown(
                """
                # The Browser
                ### Hi there, is the internet overwhelming for you?
                ### Browse everything on the internet through the Browser! Turn your open tabs into outcomes.
                """,
                elem_classes=["header-text"],
            )

        with gr.Tabs(selected="browser_use_agent") as tabs:
            with gr.TabItem("⚙️ Agent Settings", id="agent_settings"):
                create_agent_settings_tab(ui_manager)

            with gr.TabItem("⚙️ Browser Settings", id="browser_settings"):
                create_browser_settings_tab(ui_manager)

            with gr.TabItem("🌐 Browser Use", id="browser_use_agent"):
                create_browser_use_agent_tab(ui_manager)

            with gr.TabItem("🪩 Agent Hub", id="agent_hub"):
                gr.Markdown(
                    """
                    ### Turn your open tabs into a research assistant, a study partner, a travel agent, and more!
                    """,
                    elem_classes=["tab-header-text"],
                )
                with gr.Tabs():
                    with gr.TabItem("🔬 Deep Research"):
                        create_deep_research_agent_tab(ui_manager)

            # with gr.TabItem("📁 Load & Save Config"):
            #     create_load_save_config_tab(ui_manager)

    return demo
