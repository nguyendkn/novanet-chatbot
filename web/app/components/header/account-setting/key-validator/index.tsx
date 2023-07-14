import { useState } from 'react'
import Operate from './Operate'
import KeyInput from './KeyInput'
import { useValidate } from './hooks'
import type { Form, KeyFrom, Status, ValidateValue } from './declarations'
import { useKeyValidatorContext } from '@/context/key-validator'
import { LinkExternal02 } from '@/app/components/base/icons/src/vender/line/general'

export type KeyValidatorProps = {
  type: string
  title: React.ReactNode
  status: Status
  forms: Form[]
  keyFrom: KeyFrom
  onSave: (v: ValidateValue) => Promise<boolean | undefined>
}

const KeyValidator = ({
  type,
  title,
  status,
  forms,
  keyFrom,
  onSave,
}: KeyValidatorProps) => {
  const { trigger } = useKeyValidatorContext()
  const [isOpen, setIsOpen] = useState(false)
  const prevValue = forms.reduce((prev: ValidateValue, next: Form) => {
    prev[next.key] = next.value
    return prev
  }, {})
  const [value, setValue] = useState(prevValue)
  const [validate, validating, validatedStatusState] = useValidate(value)

  trigger?.useSubscription((v) => {
    if (v !== type) {
      setIsOpen(false)
      setValue(prevValue)
      validate({ before: () => false })
    }
  })

  const handleCancel = () => {
    trigger?.emit('')
  }

  const handleSave = async () => {
    if (await onSave(value))
      trigger?.emit('')
  }

  const handleAdd = () => {
    setIsOpen(true)
    trigger?.emit(type)
  }

  const handleEdit = () => {
    setIsOpen(true)
    trigger?.emit(type)
  }

  const handleChange = (form: Form, val: string) => {
    setValue({ ...value, [form.key]: val })

    if (form.validate)
      validate(form.validate)
  }

  const handleFocus = (form: Form) => {
    if (form.handleFocus)
      form.handleFocus(value, setValue)
  }

  return (
    <div className='mb-2 border-[0.5px] border-gray-200 bg-gray-50 rounded-md'>
      <div className={
        `flex items-center justify-between px-4 h-[52px] cursor-pointer ${isOpen && 'border-b-[0.5px] border-b-gray-200'}`
      }>
        {title}
        <Operate
          isOpen={isOpen}
          status={status}
          onCancel={handleCancel}
          onSave={handleSave}
          onAdd={handleAdd}
          onEdit={handleEdit}
        />
      </div>
      {
        isOpen && (
          <div className='px-4 py-3'>
            {
              forms.map(form => (
                <KeyInput
                  key={form.key}
                  className='mb-4'
                  name={form.title}
                  placeholder={form.placeholder}
                  value={value[form.key] || ''}
                  onChange={v => handleChange(form, v)}
                  onFocus={() => handleFocus(form)}
                  validating={validating}
                  validatedStatusState={validatedStatusState}
                />
              ))
            }
            <a className="flex items-center text-xs cursor-pointer text-primary-600" href={keyFrom.link} target={'_blank'}>
              {keyFrom.text}
              <LinkExternal02 className='w-3 h-3 ml-1 text-primary-600' />
            </a>
          </div>
        )
      }
    </div>
  )
}

export default KeyValidator
