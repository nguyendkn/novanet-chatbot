import json

from flask import current_app, request
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID

from core.file.upload_file_parser import UploadFileParser
from libs.helper import generate_string
from extensions.ext_database import db
from .account import Account, Tenant


class ChatbotSetup(db.Model):
    __tablename__ = 'chatbot_setups'
    __table_args__ = (
        db.PrimaryKeyConstraint('version', name='chatbot_setup_pkey'),
    )

    version = db.Column(db.String(255), nullable=False)
    setup_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))


class App(db.Model):
    __tablename__ = 'apps'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='app_pkey'),
        db.Index('app_tenant_id_idx', 'tenant_id')
    )

    id = db.Column(UUID, server_default=db.text('uuid_generate_v4()'))
    tenant_id = db.Column(UUID, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    mode = db.Column(db.String(255), nullable=False)
    icon = db.Column(db.String(255))
    icon_background = db.Column(db.String(255))
    app_model_config_id = db.Column(UUID, nullable=True)
    status = db.Column(db.String(255), nullable=False, server_default=db.text("'normal'::character varying"))
    enable_site = db.Column(db.Boolean, nullable=False)
    enable_api = db.Column(db.Boolean, nullable=False)
    api_rpm = db.Column(db.Integer, nullable=False)
    api_rph = db.Column(db.Integer, nullable=False)
    is_demo = db.Column(db.Boolean, nullable=False, server_default=db.text('false'))
    is_public = db.Column(db.Boolean, nullable=False, server_default=db.text('false'))
    is_universal = db.Column(db.Boolean, nullable=False, server_default=db.text('false'))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))

    @property
    def site(self):
        site = db.session.query(Site).filter(Site.app_id == self.id).first()
        return site

    @property
    def app_model_config(self):
        app_model_config = db.session.query(AppModelConfig).filter(
            AppModelConfig.id == self.app_model_config_id).first()
        return app_model_config

    @property
    def api_base_url(self):
        return (current_app.config['SERVICE_API_URL'] if current_app.config['SERVICE_API_URL']
                else request.host_url.rstrip('/')) + '/v1'

    @property
    def tenant(self):
        tenant = db.session.query(Tenant).filter(Tenant.id == self.tenant_id).first()
        return tenant


class AppModelConfig(db.Model):
    __tablename__ = 'app_model_configs'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='app_model_config_pkey'),
        db.Index('app_app_id_idx', 'app_id')
    )

    id = db.Column(UUID, server_default=db.text('uuid_generate_v4()'))
    app_id = db.Column(UUID, nullable=False)
    provider = db.Column(db.String(255), nullable=False)
    model_id = db.Column(db.String(255), nullable=False)
    configs = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    opening_statement = db.Column(db.Text)
    suggested_questions = db.Column(db.Text)
    suggested_questions_after_answer = db.Column(db.Text)
    speech_to_text = db.Column(db.Text)
    more_like_this = db.Column(db.Text)
    model = db.Column(db.Text)
    user_input_form = db.Column(db.Text)
    dataset_query_variable = db.Column(db.String(255))
    pre_prompt = db.Column(db.Text)
    agent_mode = db.Column(db.Text)
    sensitive_word_avoidance = db.Column(db.Text)
    retriever_resource = db.Column(db.Text)
    prompt_type = db.Column(db.String(255), nullable=False, default='simple')
    chat_prompt_config = db.Column(db.Text)
    completion_prompt_config = db.Column(db.Text)
    dataset_configs = db.Column(db.Text)
    external_data_tools = db.Column(db.Text)
    file_upload = db.Column(db.Text)

    @property
    def app(self):
        app = db.session.query(App).filter(App.id == self.app_id).first()
        return app

    @property
    def model_dict(self) -> dict:
        return json.loads(self.model) if self.model else None

    @property
    def suggested_questions_list(self) -> list:
        return json.loads(self.suggested_questions) if self.suggested_questions else []

    @property
    def suggested_questions_after_answer_dict(self) -> dict:
        return json.loads(self.suggested_questions_after_answer) if self.suggested_questions_after_answer \
            else {"enabled": False}

    @property
    def speech_to_text_dict(self) -> dict:
        return json.loads(self.speech_to_text) if self.speech_to_text \
            else {"enabled": False}

    @property
    def retriever_resource_dict(self) -> dict:
        return json.loads(self.retriever_resource) if self.retriever_resource \
            else {"enabled": False}

    @property
    def more_like_this_dict(self) -> dict:
        return json.loads(self.more_like_this) if self.more_like_this else {"enabled": False}

    @property
    def sensitive_word_avoidance_dict(self) -> dict:
        return json.loads(self.sensitive_word_avoidance) if self.sensitive_word_avoidance \
            else {"enabled": False, "type": "", "configs": []}

    @property
    def external_data_tools_list(self) -> list[dict]:
        return json.loads(self.external_data_tools) if self.external_data_tools \
            else []

    @property
    def user_input_form_list(self) -> dict:
        return json.loads(self.user_input_form) if self.user_input_form else []

    @property
    def agent_mode_dict(self) -> dict:
        return json.loads(self.agent_mode) if self.agent_mode else {"enabled": False, "strategy": None, "tools": []}

    @property
    def chat_prompt_config_dict(self) -> dict:
        return json.loads(self.chat_prompt_config) if self.chat_prompt_config else {}

    @property
    def completion_prompt_config_dict(self) -> dict:
        return json.loads(self.completion_prompt_config) if self.completion_prompt_config else {}

    @property
    def dataset_configs_dict(self) -> dict:
        return json.loads(self.dataset_configs) if self.dataset_configs else {"top_k": 2, "score_threshold": {"enable": False}}

    @property
    def file_upload_dict(self) -> dict:
        return json.loads(self.file_upload) if self.file_upload else {"image": {"enabled": False, "number_limits": 3, "detail": "high", "transfer_methods": ["remote_url", "local_file"]}}

    def to_dict(self) -> dict:
        return {
            "provider": "",
            "model_id": "",
            "configs": {},
            "opening_statement": self.opening_statement,
            "suggested_questions": self.suggested_questions_list,
            "suggested_questions_after_answer": self.suggested_questions_after_answer_dict,
            "speech_to_text": self.speech_to_text_dict,
            "retriever_resource": self.retriever_resource_dict,
            "more_like_this": self.more_like_this_dict,
            "sensitive_word_avoidance": self.sensitive_word_avoidance_dict,
            "external_data_tools": self.external_data_tools_list,
            "model": self.model_dict,
            "user_input_form": self.user_input_form_list,
            "dataset_query_variable": self.dataset_query_variable,
            "pre_prompt": self.pre_prompt,
            "agent_mode": self.agent_mode_dict,
            "prompt_type": self.prompt_type,
            "chat_prompt_config": self.chat_prompt_config_dict,
            "completion_prompt_config": self.completion_prompt_config_dict,
            "dataset_configs": self.dataset_configs_dict,
            "file_upload": self.file_upload_dict
        }

    def from_model_config_dict(self, model_config: dict):
        self.provider = ""
        self.model_id = ""
        self.configs = {}
        self.opening_statement = model_config['opening_statement']
        self.suggested_questions = json.dumps(model_config['suggested_questions'])
        self.suggested_questions_after_answer = json.dumps(model_config['suggested_questions_after_answer'])
        self.speech_to_text = json.dumps(model_config['speech_to_text']) \
            if model_config.get('speech_to_text') else None
        self.more_like_this = json.dumps(model_config['more_like_this'])
        self.sensitive_word_avoidance = json.dumps(model_config['sensitive_word_avoidance']) \
            if model_config.get('sensitive_word_avoidance') else None
        self.external_data_tools = json.dumps(model_config['external_data_tools']) \
            if model_config.get('external_data_tools') else None
        self.model = json.dumps(model_config['model'])
        self.user_input_form = json.dumps(model_config['user_input_form'])
        self.dataset_query_variable = model_config.get('dataset_query_variable')
        self.pre_prompt = model_config['pre_prompt']
        self.agent_mode = json.dumps(model_config['agent_mode'])
        self.retriever_resource = json.dumps(model_config['retriever_resource']) \
            if model_config.get('retriever_resource') else None
        self.prompt_type = model_config.get('prompt_type', 'simple')
        self.chat_prompt_config = json.dumps(model_config.get('chat_prompt_config')) \
            if model_config.get('chat_prompt_config') else None
        self.completion_prompt_config = json.dumps(model_config.get('completion_prompt_config')) \
            if model_config.get('completion_prompt_config') else None
        self.dataset_configs = json.dumps(model_config.get('dataset_configs')) \
            if model_config.get('dataset_configs') else None
        self.file_upload = json.dumps(model_config.get('file_upload')) \
            if model_config.get('file_upload') else None
        return self

    def copy(self):
        new_app_model_config = AppModelConfig(
            id=self.id,
            app_id=self.app_id,
            provider="",
            model_id="",
            configs={},
            opening_statement=self.opening_statement,
            suggested_questions=self.suggested_questions,
            suggested_questions_after_answer=self.suggested_questions_after_answer,
            speech_to_text=self.speech_to_text,
            more_like_this=self.more_like_this,
            sensitive_word_avoidance=self.sensitive_word_avoidance,
            external_data_tools=self.external_data_tools,
            model=self.model,
            user_input_form=self.user_input_form,
            dataset_query_variable=self.dataset_query_variable,
            pre_prompt=self.pre_prompt,
            agent_mode=self.agent_mode,
            retriever_resource=self.retriever_resource,
            prompt_type=self.prompt_type,
            chat_prompt_config=self.chat_prompt_config,
            completion_prompt_config=self.completion_prompt_config,
            dataset_configs=self.dataset_configs,
            file_upload=self.file_upload
        )

        return new_app_model_config


class RecommendedApp(db.Model):
    __tablename__ = 'recommended_apps'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='recommended_app_pkey'),
        db.Index('recommended_app_app_id_idx', 'app_id'),
        db.Index('recommended_app_is_listed_idx', 'is_listed', 'language')
    )

    id = db.Column(UUID, primary_key=True, server_default=db.text('uuid_generate_v4()'))
    app_id = db.Column(UUID, nullable=False)
    description = db.Column(db.JSON, nullable=False)
    copyright = db.Column(db.String(255), nullable=False)
    privacy_policy = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    position = db.Column(db.Integer, nullable=False, default=0)
    is_listed = db.Column(db.Boolean, nullable=False, default=True)
    install_count = db.Column(db.Integer, nullable=False, default=0)
    language = db.Column(db.String(255), nullable=False, server_default=db.text("'en-US'::character varying"))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))

    @property
    def app(self):
        app = db.session.query(App).filter(App.id == self.app_id).first()
        return app


class InstalledApp(db.Model):
    __tablename__ = 'installed_apps'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='installed_app_pkey'),
        db.Index('installed_app_tenant_id_idx', 'tenant_id'),
        db.Index('installed_app_app_id_idx', 'app_id'),
        db.UniqueConstraint('tenant_id', 'app_id', name='unique_tenant_app')
    )

    id = db.Column(UUID, server_default=db.text('uuid_generate_v4()'))
    tenant_id = db.Column(UUID, nullable=False)
    app_id = db.Column(UUID, nullable=False)
    app_owner_tenant_id = db.Column(UUID, nullable=False)
    position = db.Column(db.Integer, nullable=False, default=0)
    is_pinned = db.Column(db.Boolean, nullable=False, server_default=db.text('false'))
    last_used_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))

    @property
    def app(self):
        app = db.session.query(App).filter(App.id == self.app_id).first()
        return app

    @property
    def tenant(self):
        tenant = db.session.query(Tenant).filter(Tenant.id == self.tenant_id).first()
        return tenant


class Conversation(db.Model):
    __tablename__ = 'conversations'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='conversation_pkey'),
        db.Index('conversation_app_from_user_idx', 'app_id', 'from_source', 'from_end_user_id')
    )

    id = db.Column(UUID, server_default=db.text('uuid_generate_v4()'))
    app_id = db.Column(UUID, nullable=False)
    app_model_config_id = db.Column(UUID, nullable=False)
    model_provider = db.Column(db.String(255), nullable=False)
    override_model_configs = db.Column(db.Text)
    model_id = db.Column(db.String(255), nullable=False)
    mode = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.Text)
    inputs = db.Column(db.JSON)
    introduction = db.Column(db.Text)
    system_instruction = db.Column(db.Text)
    system_instruction_tokens = db.Column(db.Integer, nullable=False, server_default=db.text('0'))
    status = db.Column(db.String(255), nullable=False)
    from_source = db.Column(db.String(255), nullable=False)
    from_end_user_id = db.Column(UUID)
    from_account_id = db.Column(UUID)
    read_at = db.Column(db.DateTime)
    read_account_id = db.Column(UUID)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))

    messages = db.relationship("Message", backref="conversation", lazy='select', passive_deletes="all")
    message_annotations = db.relationship("MessageAnnotation", backref="conversation", lazy='select',
                                          passive_deletes="all")

    is_deleted = db.Column(db.Boolean, nullable=False, server_default=db.text('false'))

    @property
    def model_config(self):
        model_config = {}
        if self.override_model_configs:
            override_model_configs = json.loads(self.override_model_configs)

            if 'model' in override_model_configs:
                app_model_config = AppModelConfig()
                app_model_config = app_model_config.from_model_config_dict(override_model_configs)
                model_config = app_model_config.to_dict()
            else:
                model_config['configs'] = override_model_configs
        else:
            app_model_config = db.session.query(AppModelConfig).filter(
                AppModelConfig.id == self.app_model_config_id).first()

            model_config = app_model_config.to_dict()

        model_config['model_id'] = self.model_id
        model_config['provider'] = self.model_provider

        return model_config

    @property
    def summary_or_query(self):
        if self.summary:
            return self.summary
        else:
            first_message = self.first_message
            if first_message:
                return first_message.query
            else:
                return ''

    @property
    def annotated(self):
        return db.session.query(MessageAnnotation).filter(MessageAnnotation.conversation_id == self.id).count() > 0

    @property
    def annotation(self):
        return db.session.query(MessageAnnotation).filter(MessageAnnotation.conversation_id == self.id).first()

    @property
    def message_count(self):
        return db.session.query(Message).filter(Message.conversation_id == self.id).count()

    @property
    def user_feedback_stats(self):
        like = db.session.query(MessageFeedback) \
            .filter(MessageFeedback.conversation_id == self.id,
                    MessageFeedback.from_source == 'user',
                    MessageFeedback.rating == 'like').count()

        dislike = db.session.query(MessageFeedback) \
            .filter(MessageFeedback.conversation_id == self.id,
                    MessageFeedback.from_source == 'user',
                    MessageFeedback.rating == 'dislike').count()

        return {'like': like, 'dislike': dislike}

    @property
    def admin_feedback_stats(self):
        like = db.session.query(MessageFeedback) \
            .filter(MessageFeedback.conversation_id == self.id,
                    MessageFeedback.from_source == 'admin',
                    MessageFeedback.rating == 'like').count()

        dislike = db.session.query(MessageFeedback) \
            .filter(MessageFeedback.conversation_id == self.id,
                    MessageFeedback.from_source == 'admin',
                    MessageFeedback.rating == 'dislike').count()

        return {'like': like, 'dislike': dislike}

    @property
    def first_message(self):
        return db.session.query(Message).filter(Message.conversation_id == self.id).first()

    @property
    def app(self):
        return db.session.query(App).filter(App.id == self.app_id).first()

    @property
    def from_end_user_session_id(self):
        if self.from_end_user_id:
            end_user = db.session.query(EndUser).filter(EndUser.id == self.from_end_user_id).first()
            if end_user:
                return end_user.session_id

        return None

    @property
    def in_debug_mode(self):
        return self.override_model_configs is not None


class Message(db.Model):
    __tablename__ = 'messages'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='message_pkey'),
        db.Index('message_app_id_idx', 'app_id', 'created_at'),
        db.Index('message_conversation_id_idx', 'conversation_id'),
        db.Index('message_end_user_idx', 'app_id', 'from_source', 'from_end_user_id'),
        db.Index('message_account_idx', 'app_id', 'from_source', 'from_account_id'),
    )

    id = db.Column(UUID, server_default=db.text('uuid_generate_v4()'))
    app_id = db.Column(UUID, nullable=False)
    model_provider = db.Column(db.String(255), nullable=False)
    model_id = db.Column(db.String(255), nullable=False)
    override_model_configs = db.Column(db.Text)
    conversation_id = db.Column(UUID, db.ForeignKey('conversations.id'), nullable=False)
    inputs = db.Column(db.JSON)
    query = db.Column(db.Text, nullable=False)
    message = db.Column(db.JSON, nullable=False)
    message_tokens = db.Column(db.Integer, nullable=False, server_default=db.text('0'))
    message_unit_price = db.Column(db.Numeric(10, 4), nullable=False)
    message_price_unit = db.Column(db.Numeric(10, 7), nullable=False, server_default=db.text('0.001'))
    answer = db.Column(db.Text, nullable=False)
    answer_tokens = db.Column(db.Integer, nullable=False, server_default=db.text('0'))
    answer_unit_price = db.Column(db.Numeric(10, 4), nullable=False)
    answer_price_unit = db.Column(db.Numeric(10, 7), nullable=False, server_default=db.text('0.001'))
    provider_response_latency = db.Column(db.Float, nullable=False, server_default=db.text('0'))
    total_price = db.Column(db.Numeric(10, 7))
    currency = db.Column(db.String(255), nullable=False)
    from_source = db.Column(db.String(255), nullable=False)
    from_end_user_id = db.Column(UUID)
    from_account_id = db.Column(UUID)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    agent_based = db.Column(db.Boolean, nullable=False, server_default=db.text('false'))

    @property
    def user_feedback(self):
        feedback = db.session.query(MessageFeedback).filter(MessageFeedback.message_id == self.id,
                                                            MessageFeedback.from_source == 'user').first()
        return feedback

    @property
    def admin_feedback(self):
        feedback = db.session.query(MessageFeedback).filter(MessageFeedback.message_id == self.id,
                                                            MessageFeedback.from_source == 'admin').first()
        return feedback

    @property
    def feedbacks(self):
        feedbacks = db.session.query(MessageFeedback).filter(MessageFeedback.message_id == self.id).all()
        return feedbacks

    @property
    def annotation(self):
        annotation = db.session.query(MessageAnnotation).filter(MessageAnnotation.message_id == self.id).first()
        return annotation

    @property
    def app_model_config(self):
        conversation = db.session.query(Conversation).filter(Conversation.id == self.conversation_id).first()
        if conversation:
            return db.session.query(AppModelConfig).filter(
                AppModelConfig.id == conversation.app_model_config_id).first()

        return None

    @property
    def in_debug_mode(self):
        return self.override_model_configs is not None

    @property
    def agent_thoughts(self):
        return db.session.query(MessageAgentThought).filter(MessageAgentThought.message_id == self.id) \
            .order_by(MessageAgentThought.position.asc()).all()

    @property
    def retriever_resources(self):
        return db.session.query(DatasetRetrieverResource).filter(DatasetRetrieverResource.message_id == self.id) \
            .order_by(DatasetRetrieverResource.position.asc()).all()

    @property
    def message_files(self):
        return db.session.query(MessageFile).filter(MessageFile.message_id == self.id).all()

    @property
    def files(self):
        message_files = self.message_files

        files = []
        for message_file in message_files:
            url = message_file.url
            if message_file.type == 'image':
                if message_file.transfer_method == 'local_file':
                    upload_file = (db.session.query(UploadFile)
                                   .filter(
                        UploadFile.id == message_file.upload_file_id
                    ).first())

                    url = UploadFileParser.get_image_data(
                        upload_file=upload_file,
                        force_url=True
                    )

            files.append({
                'id': message_file.id,
                'type': message_file.type,
                'url': url
            })

        return files


class MessageFeedback(db.Model):
    __tablename__ = 'message_feedbacks'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='message_feedback_pkey'),
        db.Index('message_feedback_app_idx', 'app_id'),
        db.Index('message_feedback_message_idx', 'message_id', 'from_source'),
        db.Index('message_feedback_conversation_idx', 'conversation_id', 'from_source', 'rating')
    )

    id = db.Column(UUID, server_default=db.text('uuid_generate_v4()'))
    app_id = db.Column(UUID, nullable=False)
    conversation_id = db.Column(UUID, nullable=False)
    message_id = db.Column(UUID, nullable=False)
    rating = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text)
    from_source = db.Column(db.String(255), nullable=False)
    from_end_user_id = db.Column(UUID)
    from_account_id = db.Column(UUID)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))

    @property
    def from_account(self):
        account = db.session.query(Account).filter(Account.id == self.from_account_id).first()
        return account


class MessageFile(db.Model):
    __tablename__ = 'message_files'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='message_file_pkey'),
        db.Index('message_file_message_idx', 'message_id'),
        db.Index('message_file_created_by_idx', 'created_by')
    )

    id = db.Column(UUID, server_default=db.text('uuid_generate_v4()'))
    message_id = db.Column(UUID, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    transfer_method = db.Column(db.String(255), nullable=False)
    url = db.Column(db.Text, nullable=True)
    upload_file_id = db.Column(UUID, nullable=True)
    created_by_role = db.Column(db.String(255), nullable=False)
    created_by = db.Column(UUID, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))


class MessageAnnotation(db.Model):
    __tablename__ = 'message_annotations'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='message_annotation_pkey'),
        db.Index('message_annotation_app_idx', 'app_id'),
        db.Index('message_annotation_conversation_idx', 'conversation_id'),
        db.Index('message_annotation_message_idx', 'message_id')
    )

    id = db.Column(UUID, server_default=db.text('uuid_generate_v4()'))
    app_id = db.Column(UUID, nullable=False)
    conversation_id = db.Column(UUID, db.ForeignKey('conversations.id'), nullable=False)
    message_id = db.Column(UUID, nullable=False)
    content = db.Column(db.Text, nullable=False)
    account_id = db.Column(UUID, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))

    @property
    def account(self):
        account = db.session.query(Account).filter(Account.id == self.account_id).first()
        return account


class OperationLog(db.Model):
    __tablename__ = 'operation_logs'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='operation_log_pkey'),
        db.Index('operation_log_account_action_idx', 'tenant_id', 'account_id', 'action')
    )

    id = db.Column(UUID, server_default=db.text('uuid_generate_v4()'))
    tenant_id = db.Column(UUID, nullable=False)
    account_id = db.Column(UUID, nullable=False)
    action = db.Column(db.String(255), nullable=False)
    content = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    created_ip = db.Column(db.String(255), nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))


class EndUser(UserMixin, db.Model):
    __tablename__ = 'end_users'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='end_user_pkey'),
        db.Index('end_user_session_id_idx', 'session_id', 'type'),
        db.Index('end_user_tenant_session_id_idx', 'tenant_id', 'session_id', 'type'),
    )

    id = db.Column(UUID, server_default=db.text('uuid_generate_v4()'))
    tenant_id = db.Column(UUID, nullable=False)
    app_id = db.Column(UUID, nullable=True)
    type = db.Column(db.String(255), nullable=False)
    external_user_id = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255))
    is_anonymous = db.Column(db.Boolean, nullable=False, server_default=db.text('true'))
    session_id = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))


class Site(db.Model):
    __tablename__ = 'sites'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='site_pkey'),
        db.Index('site_app_id_idx', 'app_id'),
        db.Index('site_code_idx', 'code', 'status')
    )

    id = db.Column(UUID, server_default=db.text('uuid_generate_v4()'))
    app_id = db.Column(UUID, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    icon = db.Column(db.String(255))
    icon_background = db.Column(db.String(255))
    description = db.Column(db.String(255))
    default_language = db.Column(db.String(255), nullable=False)
    copyright = db.Column(db.String(255))
    privacy_policy = db.Column(db.String(255))
    customize_domain = db.Column(db.String(255))
    customize_token_strategy = db.Column(db.String(255), nullable=False)
    prompt_public = db.Column(db.Boolean, nullable=False, server_default=db.text('false'))
    status = db.Column(db.String(255), nullable=False, server_default=db.text("'normal'::character varying"))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    code = db.Column(db.String(255))

    @staticmethod
    def generate_code(n):
        while True:
            result = generate_string(n)
            while db.session.query(Site).filter(Site.code == result).count() > 0:
                result = generate_string(n)

            return result

    @property
    def app_base_url(self):
        return (
            current_app.config['APP_WEB_URL'] if current_app.config['APP_WEB_URL'] else request.host_url.rstrip('/'))


class ApiToken(db.Model):
    __tablename__ = 'api_tokens'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='api_token_pkey'),
        db.Index('api_token_app_id_type_idx', 'app_id', 'type'),
        db.Index('api_token_token_idx', 'token', 'type'),
        db.Index('api_token_tenant_idx', 'tenant_id', 'type')
    )

    id = db.Column(UUID, server_default=db.text('uuid_generate_v4()'))
    app_id = db.Column(UUID, nullable=True)
    tenant_id = db.Column(UUID, nullable=True)
    type = db.Column(db.String(16), nullable=False)
    token = db.Column(db.String(255), nullable=False)
    last_used_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))

    @staticmethod
    def generate_api_key(prefix, n):
        while True:
            result = prefix + generate_string(n)
            while db.session.query(ApiToken).filter(ApiToken.token == result).count() > 0:
                result = prefix + generate_string(n)

            return result


class UploadFile(db.Model):
    __tablename__ = 'upload_files'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='upload_file_pkey'),
        db.Index('upload_file_tenant_idx', 'tenant_id')
    )

    id = db.Column(UUID, server_default=db.text('uuid_generate_v4()'))
    tenant_id = db.Column(UUID, nullable=False)
    storage_type = db.Column(db.String(255), nullable=False)
    key = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    extension = db.Column(db.String(255), nullable=False)
    mime_type = db.Column(db.String(255), nullable=True)
    created_by_role = db.Column(db.String(255), nullable=False, server_default=db.text("'account'::character varying"))
    created_by = db.Column(UUID, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
    used = db.Column(db.Boolean, nullable=False, server_default=db.text('false'))
    used_by = db.Column(UUID, nullable=True)
    used_at = db.Column(db.DateTime, nullable=True)
    hash = db.Column(db.String(255), nullable=True)


class ApiRequest(db.Model):
    __tablename__ = 'api_requests'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='api_request_pkey'),
        db.Index('api_request_token_idx', 'tenant_id', 'api_token_id')
    )

    id = db.Column(UUID, nullable=False, server_default=db.text('uuid_generate_v4()'))
    tenant_id = db.Column(UUID, nullable=False)
    api_token_id = db.Column(UUID, nullable=False)
    path = db.Column(db.String(255), nullable=False)
    request = db.Column(db.Text, nullable=True)
    response = db.Column(db.Text, nullable=True)
    ip = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))


class MessageChain(db.Model):
    __tablename__ = 'message_chains'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='message_chain_pkey'),
        db.Index('message_chain_message_id_idx', 'message_id')
    )

    id = db.Column(UUID, nullable=False, server_default=db.text('uuid_generate_v4()'))
    message_id = db.Column(UUID, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    input = db.Column(db.Text, nullable=True)
    output = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())


class MessageAgentThought(db.Model):
    __tablename__ = 'message_agent_thoughts'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='message_agent_thought_pkey'),
        db.Index('message_agent_thought_message_id_idx', 'message_id'),
        db.Index('message_agent_thought_message_chain_id_idx', 'message_chain_id'),
    )

    id = db.Column(UUID, nullable=False, server_default=db.text('uuid_generate_v4()'))
    message_id = db.Column(UUID, nullable=False)
    message_chain_id = db.Column(UUID, nullable=False)
    position = db.Column(db.Integer, nullable=False)
    thought = db.Column(db.Text, nullable=True)
    tool = db.Column(db.Text, nullable=True)
    tool_input = db.Column(db.Text, nullable=True)
    observation = db.Column(db.Text, nullable=True)
    # plugin_id = db.Column(UUID, nullable=True)  ## for future design
    tool_process_data = db.Column(db.Text, nullable=True)
    message = db.Column(db.Text, nullable=True)
    message_token = db.Column(db.Integer, nullable=True)
    message_unit_price = db.Column(db.Numeric, nullable=True)
    message_price_unit = db.Column(db.Numeric(10, 7), nullable=False, server_default=db.text('0.001'))
    answer = db.Column(db.Text, nullable=True)
    answer_token = db.Column(db.Integer, nullable=True)
    answer_unit_price = db.Column(db.Numeric, nullable=True)
    answer_price_unit = db.Column(db.Numeric(10, 7), nullable=False, server_default=db.text('0.001'))
    tokens = db.Column(db.Integer, nullable=True)
    total_price = db.Column(db.Numeric, nullable=True)
    currency = db.Column(db.String, nullable=True)
    latency = db.Column(db.Float, nullable=True)
    created_by_role = db.Column(db.String, nullable=False)
    created_by = db.Column(UUID, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())


class DatasetRetrieverResource(db.Model):
    __tablename__ = 'dataset_retriever_resources'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='dataset_retriever_resource_pkey'),
        db.Index('dataset_retriever_resource_message_id_idx', 'message_id'),
    )

    id = db.Column(UUID, nullable=False, server_default=db.text('uuid_generate_v4()'))
    message_id = db.Column(UUID, nullable=False)
    position = db.Column(db.Integer, nullable=False)
    dataset_id = db.Column(UUID, nullable=False)
    dataset_name = db.Column(db.Text, nullable=False)
    document_id = db.Column(UUID, nullable=False)
    document_name = db.Column(db.Text, nullable=False)
    data_source_type = db.Column(db.Text, nullable=False)
    segment_id = db.Column(UUID, nullable=False)
    score = db.Column(db.Float, nullable=True)
    content = db.Column(db.Text, nullable=False)
    hit_count = db.Column(db.Integer, nullable=True)
    word_count = db.Column(db.Integer, nullable=True)
    segment_position = db.Column(db.Integer, nullable=True)
    index_node_hash = db.Column(db.Text, nullable=True)
    retriever_from = db.Column(db.Text, nullable=False)
    created_by = db.Column(UUID, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())
