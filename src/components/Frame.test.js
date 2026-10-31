import { describe, it, expect } from 'vitest'
import { evaluateExpression } from './Frame'

describe('Calculator Expression Evaluator (evaluateExpression)', () => {
  it('correctly performs addition', () => {
    expect(evaluateExpression('5+3')).toBe('8')
    expect(evaluateExpression('10 + 25')).toBe('35')
  })

  it('correctly performs subtraction', () => {
    expect(evaluateExpression('15-7')).toBe('8')
    expect(evaluateExpression('5 - 12')).toBe('-7')
  })

  it('correctly performs multiplication', () => {
    expect(evaluateExpression('6*7')).toBe('42')
    expect(evaluateExpression('0 * 100')).toBe('0')
  })

  it('correctly performs division', () => {
    expect(evaluateExpression('20/4')).toBe('5')
    expect(evaluateExpression('9 / 2')).toBe('4.5')
  })

  it('handles operator precedence correctly (order of operations)', () => {
    expect(evaluateExpression('2+3*4')).toBe('14')
    expect(evaluateExpression('(2+3)*4')).toBe('20')
  })

  it('handles decimals properly', () => {
    expect(evaluateExpression('1.5 + 2.5')).toBe('4')
    expect(evaluateExpression('0.1 + 0.2')).toMatch(/^0\.3/)
  })

  it('returns Error on division by zero', () => {
    expect(evaluateExpression('10/0')).toBe('Error')
  })

  it('returns Error on invalid syntax or unclosed parentheses', () => {
    expect(evaluateExpression('5++')).toBe('Error')
    expect(evaluateExpression('(5+2')).toBe('Error')
  })

  it('rejects malicious characters or code injection attempts', () => {
    expect(evaluateExpression('alert("hack")')).toBe('Error')
    expect(evaluateExpression('process.exit()')).toBe('Error')
    expect(evaluateExpression('window.location')).toBe('Error')
  })
})
