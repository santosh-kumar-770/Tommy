console.log(
    "VEERA CONTENT SCRIPT LOADED"
);

chrome.runtime.onMessage.addListener(
    async (
        request,
        sender,
        sendResponse
    ) => {

        if (
            request.action === "scan_feed"
        ) {

            const elements =
                document.querySelectorAll(
                    '[data-testid="expandable-text-box"]'
                );

            const posts = [];

            elements.forEach(post => {

                const text =
                    post.innerText;

                if (
                    text &&
                    text.length > 50
                ) {

                    const authorElement =
                        post.parentElement
                            ?.parentElement
                            ?.querySelector("p");

                    const author =
                        authorElement?.innerText ||
                        text.split("\n")[0] ||
                        "Unknown";

                    console.log(
                        "Author Found:",
                        author
                    );

                    posts.push({
                        author: author,
                        content: text,
                        post_url: window.location.href
                    });

                }

            });

            console.log(
                "Posts Found:",
                posts
            );

            try {

                const response =
                    await fetch(
                        "http://127.0.0.1:8000/linkedin/feed-batch",
                        {
                            method: "POST",
                            headers: {
                                "Content-Type":
                                    "application/json"
                            },
                            body: JSON.stringify({
                                posts: posts
                            })
                        }
                    );

                const data =
                    await response.json();

                console.log(
                    "VEERA RESPONSE:",
                    data
                );

                sendResponse(data);

            } catch (error) {

                console.error(
                    "VEERA ERROR:",
                    error
                );

                sendResponse({
                    error:
                        error.message
                });

            }

        }

        return true;
    }
);