from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Go to DuckDuckGo
    page.goto("https://www.duckduckgo.com/")

    # Search for n8n
    search_box = "input[name='q']"
    page.fill(search_box, "n8n")
    page.press(search_box, "Enter")

    # Click the n8n website link
    n8n_link = "a:has-text('AI Workflow Automation Platform & Tools - n8n')"
    page.wait_for_selector(n8n_link, timeout=5000)
    page.click(n8n_link)

    page.wait_for_load_state("load")

    # Click 'Browse all integrations'
    browse_link = "a:has-text('Browse all integrations')"
    page.wait_for_selector(browse_link, timeout=5000)
    page.click(browse_link)

    # Search for Groq workflow
    workflow_input = "input[placeholder='Search for workflows, nodes, tasks...']"
    page.wait_for_selector(workflow_input, timeout=5000)
    page.fill(workflow_input, "Groq")
    page.press(workflow_input, "Enter")

    # Navigate directly to the Groq integration page
    page.goto("https://n8n.io/integrations/groq-chat-model")

    input("Press Enter to close the browser...")
    browser.close()