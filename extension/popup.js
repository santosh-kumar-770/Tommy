const scanButton =
    document.getElementById(
        "scanFeed"
    );

const status =
    document.getElementById(
        "status"
    );

scanButton.addEventListener(
    "click",
    async () => {

        status.textContent =
            "Scanning feed...";

        const [tab] =
            await chrome.tabs.query({
                active: true,
                currentWindow: true
            });

        chrome.tabs.sendMessage(
            tab.id,
            {
                action: "scan_feed"
            },
            (response) => {

                if (
                    chrome.runtime.lastError
                ) {

                    status.textContent =
                        "Connection failed";

                    console.error(
                        chrome.runtime
                        .lastError
                    );

                    return;
                }

                if (response?.error) {

                    status.textContent =
                        "Backend failed";

                    return;
                }

                status.textContent =
                    "Scan completed";

                console.log(
                    response
                );
            }
        );

    }
);