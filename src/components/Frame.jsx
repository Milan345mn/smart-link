import { useState } from 'react'
import Screen from './Screen'
import Button from './Button'

// Safe math expression evaluator (replaces dangerous eval)
export const evaluateExpression = (expression) => {
  try {
    // Only allow numbers, operators, and decimal points
    if (!/^[\d+\-*/.() ]+$/.test(expression)) {
      return 'Error'
    }
    // Use Function constructor as safer alternative to eval
    const result = new Function(`return ${expression}`)()
    if (!isFinite(result)) return 'Error'
    return String(result)
  } catch {
    return 'Error'
  }
}

const Frame = () => {
  const [question, setQuestion] = useState('')
  const [answer, setAnswer] = useState('')

  const handleClick = (event) => {
    const value = event.target.value
    
    switch (value) {
      case '=':
        setAnswer(evaluateExpression(question))
        break
      case 'Cls':
        setQuestion('')
        setAnswer('')
        break
      default:
        setQuestion(prev => prev + value)
        break
    }
  }

  return (
    <div className="frame">
      <div className="calculator-title">React Calculator (CI/CD Verified)</div>
      <Screen question={question} answer={answer} />
      <div className="button-row">
        <Button label="1" handleClick={handleClick} type="input" />
        <Button label="2" handleClick={handleClick} type="input" />
        <Button label="3" handleClick={handleClick} type="input" />
        <Button label="4" handleClick={handleClick} type="input" />
        <Button label="-" handleClick={handleClick} type="action" />
        <Button label="+" handleClick={handleClick} type="action" />
      </div>
      <div className="button-row">
        <Button label="5" handleClick={handleClick} type="input" />
        <Button label="6" handleClick={handleClick} type="input" />
        <Button label="7" handleClick={handleClick} type="input" />
        <Button label="8" handleClick={handleClick} type="input" />
        <Button label="*" handleClick={handleClick} type="action" />
        <Button label="/" handleClick={handleClick} type="action" />
      </div>
      <div className="button-row">
        <Button label="9" handleClick={handleClick} type="input" />
        <Button label="." handleClick={handleClick} type="input" />
        <Button label="0" handleClick={handleClick} type="input" />
        <Button label="Cls" handleClick={handleClick} type="action" />
        <Button label="=" handleClick={handleClick} type="action" />
      </div>
    </div>
  )
}

export default Frame

