const translation = {
  title: '数据集设置',
  desc: '在这里您可以修改数据集的工作方式以及其它设置。',
  form: {
    name: '数据集名称',
    namePlaceholder: '请输入数据集名称',
    nameError: '名称不能为空',
    desc: '数据集描述',
    descInfo: '请写出清楚的文字描述来概述数据集的内容。当从多个数据集中进行选择匹配时，该描述将用作匹配的基础。',
    descPlaceholder: '描述这个数据集中的内容。详细的描述可以让 AI 及时访问数据集的内容。如果为空，Chatbot 将使用默认的命中策略。',
    descWrite: '了解如何编写更好的数据集描述。',
    permissions: '可见权限',
    permissionsOnlyMe: '只有我',
    permissionsAllMember: '所有团队成员',
    indexMethod: '索引模式',
    indexMethodHighQuality: '高质量',
    indexMethodHighQualityTip: '调用 OpenAI 的嵌入接口进行处理，以在用户查询时提供更高的准确度',
    indexMethodEconomy: '经济',
    indexMethodEconomyTip: '使用离线的向量引擎、关键词索引等方式，降低了准确度但无需花费 Token',
    embeddingModel: 'Embedding 模型',
    embeddingModelTip: '修改 Embedding 模型，请去',
    embeddingModelTipLink: '设置',
    save: '保存',
  },
}

export default translation
