import React, { useEffect, useState } from 'react'
import type { FC } from 'react'
import { useTranslation } from 'react-i18next'
import {
  PencilSquareIcon,
} from '@heroicons/react/24/outline'
import cn from 'classnames'
import Button from '../../../base/button'
import List from './list'
import AppInfo from '@/app/components/share/chat/sidebar/app-info'
// import Card from './card'
import type { ConversationItem, SiteInfo } from '@/models/share'
import { fetchConversations } from '@/service/share'

export type ISidebarProps = {
  copyRight: string
  currentId: string
  onCurrentIdChange: (id: string) => void
  list: ConversationItem[]
  pinnedList: ConversationItem[]
  isInstalledApp: boolean
  installedAppId?: string
  siteInfo: SiteInfo
  onMoreLoaded: (res: { data: ConversationItem[]; has_more: boolean }) => void
  onPinnedMoreLoaded: (res: { data: ConversationItem[]; has_more: boolean }) => void
  isNoMore: boolean
  isPinnedNoMore: boolean
  onPin: (id: string) => void
  onUnpin: (id: string) => void
  controlUpdateList: number
}

const Sidebar: FC<ISidebarProps> = ({
  copyRight,
  currentId,
  onCurrentIdChange,
  list,
  pinnedList,
  isInstalledApp,
  installedAppId,
  siteInfo,
  onMoreLoaded,
  onPinnedMoreLoaded,
  isNoMore,
  isPinnedNoMore,
  onPin,
  onUnpin,
  controlUpdateList,
}) => {
  const { t } = useTranslation()
  const [hasPinned, setHasPinned] = useState(false)

  const checkHasPinned = async () => {
    const { data }: any = await fetchConversations(isInstalledApp, installedAppId, undefined, true)
    setHasPinned(data.length > 0)
  }

  useEffect(() => {
    checkHasPinned()
  }, [])

  useEffect(() => {
    if (controlUpdateList !== 0)
      checkHasPinned()
  }, [controlUpdateList])

  return (
    <div
      className={
        cn(
          isInstalledApp ? 'tablet:h-[calc(100vh_-_74px)]' : 'tablet:h-[calc(100vh_-_3rem)]',
          'shrink-0 flex flex-col bg-white pc:w-[244px] tablet:w-[192px] mobile:w-[240px]  border-r border-gray-200 mobile:h-screen',
        )
      }
    >
      {isInstalledApp && (
        <AppInfo
          className='my-4 px-4'
          name={siteInfo.title || ''}
          icon={siteInfo.icon || ''}
          icon_background={siteInfo.icon_background}
        />
      )}
      <div className="flex flex-shrink-0 p-4 !pb-0">
        <Button
          onClick={() => { onCurrentIdChange('-1') }}
          className="group block w-full flex-shrink-0 !justify-start !h-9 text-primary-600 items-center text-sm">
          <PencilSquareIcon className="mr-2 h-4 w-4" /> {t('share.chat.newChat')}
        </Button>
      </div>
      <div className='flex-grow'>
        {/* pinned list */}
        {hasPinned && (
          <div className='mt-4 px-4'>
            <div className='mb-1.5 leading-[18px] text-xs text-gray-500 font-medium uppercase'>{t('share.chat.pinnedTitle')}</div>
            <List
              className='max-h-[40vh]'
              currentId={currentId}
              onCurrentIdChange={onCurrentIdChange}
              list={pinnedList}
              isInstalledApp={isInstalledApp}
              installedAppId={installedAppId}
              onMoreLoaded={onPinnedMoreLoaded}
              isNoMore={isPinnedNoMore}
              isPinned={true}
              onPinChanged={id => onUnpin(id)}
              controlUpdate={controlUpdateList + 1}
            />
          </div>
        )}
        {/* unpinned list */}
        <div className='mt-4 px-4'>
          {hasPinned && (
            <div className='mb-1.5 leading-[18px] text-xs text-gray-500 font-medium uppercase'>{t('share.chat.unpinnedTitle')}</div>
          )}
          <List
            className={cn(hasPinned ? 'max-h-[40vh]' : 'flex-grow')}
            currentId={currentId}
            onCurrentIdChange={onCurrentIdChange}
            list={list}
            isInstalledApp={isInstalledApp}
            installedAppId={installedAppId}
            onMoreLoaded={onMoreLoaded}
            isNoMore={isNoMore}
            isPinned={false}
            onPinChanged={id => onPin(id)}
            controlUpdate={controlUpdateList + 1}
          />
        </div>
      </div>
      <div className="flex flex-shrink-0 pr-4 pb-4 pl-4">
        <div className="text-gray-400 font-normal text-xs">© {copyRight} {(new Date()).getFullYear()}</div>
      </div>
    </div>
  )
}

export default React.memo(Sidebar)
