-- Enable UUID support
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- =========================
-- USERS
-- =========================
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    whatsapp_number TEXT,
    linkedin_profile_url TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- =========================
-- PEOPLE (LinkedIn connections)
-- =========================
CREATE TABLE people (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    linkedin_person_id TEXT,
    name TEXT NOT NULL,
    company TEXT,
    headline TEXT,
    importance_score FLOAT DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- =========================
-- POSTS (Feed data)
-- =========================
CREATE TABLE posts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    author_id UUID REFERENCES people(id) ON DELETE SET NULL,
    linkedin_post_id TEXT UNIQUE,
    content TEXT,
    category TEXT,
    importance_score FLOAT,
    summary TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- =========================
-- ALERTS (WhatsApp output)
-- =========================
CREATE TABLE alerts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    post_id UUID REFERENCES posts(id) ON DELETE CASCADE,
    alert_type TEXT,
    content TEXT,
    status TEXT DEFAULT 'sent',
    created_at TIMESTAMP DEFAULT NOW()
);

-- =========================
-- CONVERSATIONS (DM threads)
-- =========================
CREATE TABLE conversations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    person_id UUID REFERENCES people(id) ON DELETE CASCADE,
    linkedin_conversation_id TEXT UNIQUE,
    last_message_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);

-- =========================
-- MESSAGES (Chat history)
-- =========================
CREATE TABLE messages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    conversation_id UUID REFERENCES conversations(id) ON DELETE CASCADE,
    sender_type TEXT CHECK (sender_type IN ('user','person','ai')),
    message_text TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- =========================
-- REPLY SUGGESTIONS (AI output)
-- =========================
CREATE TABLE reply_suggestions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    message_id UUID REFERENCES messages(id) ON DELETE CASCADE,
    reply_text TEXT,
    is_selected BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- =========================
-- INDEXES (Performance)
-- =========================
CREATE INDEX idx_posts_user ON posts(user_id);
CREATE INDEX idx_posts_category ON posts(category);
CREATE INDEX idx_messages_conversation ON messages(conversation_id);
CREATE INDEX idx_conversations_person ON conversations(person_id);
CREATE INDEX idx_people_user ON people(user_id);