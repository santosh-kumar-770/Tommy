const scanButton =
    document.getElementById(
        "scanFeed"
    );

const status =
    document.getElementById(
        "status"
    );

const resultsDiv =
    document.getElementById(
        "results"
    );

scanButton.addEventListener(
    "click",
    async () => {

        status.textContent =
            "Scanning Feed...";

        resultsDiv.innerHTML = "";

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
                        "Connection Failed";

                    console.error(
                        chrome.runtime
                            .lastError
                    );

                    return;
                }

                if (
                    !response ||
                    !response.important_posts
                ) {

                    status.textContent =
                        "No Results";

                    return;
                }

                status.textContent =
                    `Found ${response.count} Important Posts`;

                response.important_posts
                    .forEach(post => {

                        const card =
                            document.createElement(
                                "div"
                            );

                        card.style.border =
                            "1px solid #ccc";

                        card.style.padding =
                            "10px";

                        card.style.marginTop =
                            "10px";

                        card.innerHTML = `
                            <b>${post.category}</b>
                            <br><br>

                            <b>Author:</b>
                            ${post.author}

                            <br><br>

                            <b>Importance:</b>
                            ${post.importance_score}

                            <br><br>

                            <b>Summary:</b>
                            ${post.ai_analysis.summary}
                        `;

                        resultsDiv
                            .appendChild(
                                card
                            );

                    });

            }
        );

    }
);

const showReplies =
    document.getElementById(
        "showReplies"
    );

const replySection =
    document.getElementById(
        "replySection"
    );

const generateReplies =
    document.getElementById(
        "generateReplies"
    );

const replyResults =
    document.getElementById(
        "replyResults"
    );

showReplies.addEventListener(
    "click",
    () => {

        replySection.style.display =
            "block";

    }
);

generateReplies.addEventListener(
    "click",
    async () => {

        const personName =
            document.getElementById(
                "personName"
            ).value;

        const conversation =
            document.getElementById(
                "conversation"
            ).value;

        const response =
            await fetch(
                "http://127.0.0.1:8000/linkedin/suggest-replies",
                {
                    method: "POST",
                    headers: {
                        "Content-Type":
                            "application/json"
                    },
                    body: JSON.stringify({
                        person_name:
                            personName,
                        conversation: [
                            {
                                sender:
                                    "person",
                                message:
                                    conversation
                            }
                        ]
                    })
                }
            );

        const data =
            await response.json();

        replyResults.innerHTML =
            "";

        data.suggestions.forEach(
            reply => {

                const div =
                    document.createElement(
                        "div"
                    );

                div.style.border =
                    "1px solid #ccc";

                div.style.padding =
                    "10px";

                div.style.marginTop =
                    "10px";

                div.innerHTML =
                    reply;

                replyResults
                    .appendChild(
                        div
                    );

            }
        );

    }
);