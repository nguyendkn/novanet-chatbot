const translation = {
  list: {
    title: 'Documents',
    desc: 'All files of the dataset are shown here, and the entire dataset can be linked to Chatbot citations or indexed via the Chat plugin.',
    addFile: 'add file',
    addPages: 'Add Pages',
    table: {
      header: {
        fileName: 'FILE NAME',
        words: 'WORDS',
        hitCount: 'HIT COUNT',
        uploadTime: 'UPLOAD TIME',
        status: 'STATUS',
        action: 'ACTION',
      },
    },
    action: {
      uploadFile: 'Upload new file',
      settings: 'Segment settings',
      addButton: 'Add segment',
      add: 'Add a segment',
      batchAdd: 'Batch add',
      archive: 'Archive',
      unarchive: 'Unarchive',
      delete: 'Delete',
      enableWarning: 'Archived file cannot be enabled',
      sync: 'Sync',
    },
    index: {
      enable: 'Enable',
      disable: 'Disable',
      all: 'All',
      enableTip: 'The file can be indexed',
      disableTip: 'The file cannot be indexed',
    },
    status: {
      queuing: 'Queuing',
      indexing: 'Indexing',
      paused: 'Paused',
      error: 'Error',
      available: 'Available',
      enabled: 'Enabled',
      disabled: 'Disabled',
      archived: 'Archived',
    },
    empty: {
      title: 'There is no documentation yet',
      upload: {
        tip: 'You can upload files, sync from the website, or from webb apps like Notion, GitHub, etc.',
      },
      sync: {
        tip: 'Chatbot will periodically download files from your Notion and complete processing.',
      },
    },
    delete: {
      title: 'Are you sure Delete?',
      content: 'If you need to resume processing later, you will continue from where you left off',
    },
    batchModal: {
      title: 'Batch add segments',
      csvUploadTitle: 'Drag and drop your CSV file here, or ',
      browse: 'browse',
      tip: 'The CSV file must conform to the following structure:',
      question: 'question',
      answer: 'answer',
      contentTitle: 'segment content',
      content: 'content',
      template: 'Download the template here',
      cancel: 'Cancel',
      run: 'Run Batch',
      runError: 'Run batch failed',
      processing: 'In batch processing',
      completed: 'Import completed',
      error: 'Import Error',
      ok: 'OK',
    },
  },
  metadata: {
    title: 'Metadata',
    desc: 'Labeling metadata for documents allows AI to access them in a timely manner and exposes the source of references for users.',
    dateTimeFormat: 'MMMM D, YYYY hh:mm A',
    docTypeSelectTitle: 'Please select a document type',
    docTypeChangeTitle: 'Change document type',
    docTypeSelectWarning:
      'If the document type is changed, the now filled metadata will no longer be preserved',
    firstMetaAction: 'Let\'s go',
    placeholder: {
      add: 'Add ',
      select: 'Select ',
    },
    source: {
      upload_file: 'Upload File',
      notion: 'Sync form Notion',
      github: 'Sync form Github',
    },
    type: {
      book: 'Book',
      webPage: 'Web Page',
      paper: 'Paper',
      socialMediaPost: 'Social Media Post',
      personalDocument: 'Personal Document',
      businessDocument: 'Business Document',
      IMChat: 'IM Chat',
      wikipediaEntry: 'Wikipedia Entry',
      notion: 'Sync form Notion',
      github: 'Sync form Github',
      technicalParameters: 'Technical Parameters',
    },
    field: {
      processRule: {
        processDoc: 'Process Document',
        segmentRule: 'Segment Rule',
        segmentLength: 'Segment Length',
        processClean: 'Text Process Clean',
      },
      book: {
        title: 'Title',
        language: 'Language',
        author: 'Author',
        publisher: 'Publisher',
        publicationDate: 'Publication Date',
        ISBN: 'ISBN',
        category: 'Category',
      },
      webPage: {
        title: 'Title',
        url: 'URL',
        language: 'Language',
        authorPublisher: 'Author/Publisher',
        publishDate: 'Publish Date',
        topicsKeywords: 'Topics/Keywords',
        description: 'Description',
      },
      paper: {
        title: 'Title',
        language: 'Language',
        author: 'Author',
        publishDate: 'Publish Date',
        journalConferenceName: 'Journal/Conference Name',
        volumeIssuePage: 'Volume/Issue/Page',
        DOI: 'DOI',
        topicsKeywords: 'Topics/Keywords',
        abstract: 'Abstract',
      },
      socialMediaPost: {
        platform: 'Platform',
        authorUsername: 'Author/Username',
        publishDate: 'Publish Date',
        postURL: 'Post URL',
        topicsTags: 'Topics/Tags',
      },
      personalDocument: {
        title: 'Title',
        author: 'Author',
        creationDate: 'Creation Date',
        lastModifiedDate: 'Last Modified Date',
        documentType: 'Document Type',
        tagsCategory: 'Tags/Category',
      },
      businessDocument: {
        title: 'Title',
        author: 'Author',
        creationDate: 'Creation Date',
        lastModifiedDate: 'Last Modified Date',
        documentType: 'Document Type',
        departmentTeam: 'Department/Team',
      },
      IMChat: {
        chatPlatform: 'Chat Platform',
        chatPartiesGroupName: 'Chat Parties/Group Name',
        participants: 'Participants',
        startDate: 'Start Date',
        endDate: 'End Date',
        topicsKeywords: 'Topics/Keywords',
        fileType: 'File Type',
      },
      wikipediaEntry: {
        title: 'Title',
        language: 'Language',
        webpageURL: 'Webpage URL',
        editorContributor: 'Editor/Contributor',
        lastEditDate: 'Last Edit Date',
        summaryIntroduction: 'Summary/Introduction',
      },
      notion: {
        title: 'Title',
        language: 'Language',
        author: 'Author',
        createdTime: 'Created Time',
        lastModifiedTime: 'Last Modified Time',
        url: 'URL',
        tag: 'Tag',
        description: 'Description',
      },
      github: {
        repoName: 'Repo Name',
        repoDesc: 'Repo Description',
        repoOwner: 'Repo Owner',
        fileName: 'File Name',
        filePath: 'File Path',
        programmingLang: 'Programming Language',
        url: 'URL',
        license: 'License',
        lastCommitTime: 'Last Commit Time',
        lastCommitAuthor: 'Last Commit Author',
      },
      originInfo: {
        originalFilename: 'Original filename',
        originalFileSize: 'Original file size',
        uploadDate: 'Upload date',
        lastUpdateDate: 'Last update date',
        source: 'Source',
      },
      technicalParameters: {
        segmentSpecification: 'Segment specification',
        segmentLength: 'Segment length',
        avgParagraphLength: 'Avg. paragraph length',
        paragraphs: 'Paragraphs',
        hitCount: 'Hit count',
        embeddingTime: 'Embedding time',
        embeddedSpend: 'Embedded spend',
      },
    },
    languageMap: {
      zh: 'Chinese',
      en: 'English',
      es: 'Spanish',
      fr: 'French',
      de: 'German',
      ja: 'Japanese',
      ko: 'Korean',
      ru: 'Russian',
      ar: 'Arabic',
      pt: 'Portuguese',
      it: 'Italian',
      nl: 'Dutch',
      pl: 'Polish',
      sv: 'Swedish',
      tr: 'Turkish',
      he: 'Hebrew',
      hi: 'Hindi',
      da: 'Danish',
      fi: 'Finnish',
      no: 'Norwegian',
      hu: 'Hungarian',
      el: 'Greek',
      cs: 'Czech',
      th: 'Thai',
      id: 'Indonesian',
    },
    categoryMap: {
      book: {
        fiction: 'Fiction',
        biography: 'Biography',
        history: 'History',
        science: 'Science',
        technology: 'Technology',
        education: 'Education',
        philosophy: 'Philosophy',
        religion: 'Religion',
        socialSciences: 'SocialSciences',
        art: 'Art',
        travel: 'Travel',
        health: 'Health',
        selfHelp: 'SelfHelp',
        businessEconomics: 'BusinessEconomics',
        cooking: 'Cooking',
        childrenYoungAdults: 'ChildrenYoungAdults',
        comicsGraphicNovels: 'ComicsGraphicNovels',
        poetry: 'Poetry',
        drama: 'Drama',
        other: 'Other',
      },
      personalDoc: {
        notes: 'Notes',
        blogDraft: 'Blog Draft',
        diary: 'Diary',
        researchReport: 'Research Report',
        bookExcerpt: 'Book Excerpt',
        schedule: 'Schedule',
        list: 'List',
        projectOverview: 'Project Overview',
        photoCollection: 'Photo Collection',
        creativeWriting: 'Creative Writing',
        codeSnippet: 'Code Snippet',
        designDraft: 'Design Draft',
        personalResume: 'Personal Resume',
        other: 'Other',
      },
      businessDoc: {
        meetingMinutes: 'Meeting Minutes',
        researchReport: 'Research Report',
        proposal: 'Proposal',
        employeeHandbook: 'Employee Handbook',
        trainingMaterials: 'Training Materials',
        requirementsDocument: 'Requirements Document',
        designDocument: 'Design Document',
        productSpecification: 'Product Specification',
        financialReport: 'Financial Report',
        marketAnalysis: 'Market Analysis',
        projectPlan: 'Project Plan',
        teamStructure: 'Team Structure',
        policiesProcedures: 'Policies & Procedures',
        contractsAgreements: 'Contracts & Agreements',
        emailCorrespondence: 'Email Correspondence',
        other: 'Other',
      },
    },
  },
  embedding: {
    processing: 'Embedding processing...',
    paused: 'Embedding paused',
    completed: 'Embedding completed',
    error: 'Embedding error',
    docName: 'Preprocessing document',
    mode: 'Segmentation rule',
    segmentLength: 'Segmentation length',
    textCleaning: 'Text pre-definition and cleaning',
    segments: 'Paragraphs',
    highQuality: 'High-quality mode',
    economy: 'Economy mode',
    estimate: 'Estimated consumption',
    stop: 'Stop processing',
    resume: 'Resume processing',
    automatic: 'Automatic',
    custom: 'Custom',
    previewTip: 'Paragraph preview will be available after embedding is complete',
  },
  segment: {
    paragraphs: 'Paragraphs',
    keywords: 'Key Words',
    addKeyWord: 'Add key word',
    keywordError: 'The maximum length of keyword is 20',
    characters: 'characters',
    hitCount: 'hit count',
    vectorHash: 'Vector hash: ',
    questionPlaceholder: 'add question here',
    questionEmpty: 'Question can not be empty',
    answerPlaceholder: 'add answer here',
    answerEmpty: 'Answer can not be empty',
    contentPlaceholder: 'add content here',
    contentEmpty: 'Content can not be empty',
    newTextSegment: 'New Text Segment',
    newQaSegment: 'New Q&A Segment',
    delete: 'Delete this segment ?',
  },
}

export default translation
